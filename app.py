from flask import Flask, request, jsonify, send_file
import openai
import os
from docx import Document
from sentence_transformers import SentenceTransformer, util

# Configurare OpenAI

app = Flask(__name__)
DOCX_FOLDER = "MODULE"
model = SentenceTransformer('all-MiniLM-L6-v2')


def incarca_documente(folder):
    date = []
    paragraf_per_pagina = 20  # presupunem aprox. 20 paragrafe reale pe pagină
    for fisier in os.listdir(folder):
        if fisier.endswith(".docx"):
            doc_path = os.path.join(folder, fisier)
            try:
                doc = Document(doc_path)
                par_idx = 0
                for par in doc.paragraphs:
                    text = par.text.strip()
                    if text:
                        par_idx += 1
                        pagina_estimata = (par_idx - 1) // paragraf_per_pagina + 1
                        date.append({
                            "fisier": fisier,
                            "paragraf": text,
                            "index": par_idx,
                            "pagina": pagina_estimata
                        })
            except Exception as e:
                print(f"Eroare la deschiderea fișierului {fisier}: {e}")
    return date


def cauta_raspuns(intrebare, documente):
    if not documente:
        return "⚠️ No documents found.", None

    intrebare_embed = model.encode(intrebare, convert_to_tensor=True)
    paragraf_text = [d["paragraf"] for d in documente]
    paragraf_embed = model.encode(paragraf_text, convert_to_tensor=True)

    similaritati = util.cos_sim(intrebare_embed, paragraf_embed)[0]
    rezultat_idx = int(similaritati.argmax())
    scor = float(similaritati[rezultat_idx])

    if scor < 0.4:
        return "❌ No relevant result found.", None

    rezultat = documente[rezultat_idx]

    # Formulează un răspuns cu OpenAI folosind paragraful ca context
    try:
        completare = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an academic assistant who explains information in a helpful and complete way but not too long."},
                {"role": "user", "content": f"Using this excerpt from the course materials, answer the question below:\n\n{rezultat['paragraf']}\n\nQuestion: {intrebare}"}
            ],
            temperature=0.5,
            max_tokens=512
        )
        raspuns_ai = completare["choices"][0]["message"]["content"].strip()
    except Exception as e:
        raspuns_ai = f"❌ OpenAI API error: {e}"

    info = (
        f"📄 File: {rezultat['fisier']}, Paragraph: {rezultat['index']}, Estimated page: {rezultat['pagina']}\n\n"
        f"{raspuns_ai}\n(Similarity score: {scor:.2f})"
    )
    return info, scor


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question", "")
    documente = incarca_documente(DOCX_FOLDER)
    raspuns, _ = cauta_raspuns(question, documente)
    return jsonify({"answer": raspuns})


@app.route("/")
def home():
    return send_file("index_final.html")


if __name__ == "__main__":
    app.run(port=8080, debug=True)
