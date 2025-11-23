# CHATBOT
# 🤖 AI Educational Chatbot: Personalized Learning Assistant

[cite_start]This project is an advanced educational chatbot developed at the **Politehnica University of Bucharest, Faculty of Automation and Computer Science** [cite: 3, 4] [cite_start]for the Algorithms Design course[cite: 1, 16]. [cite_start]Its main goal is to provide personalized and accurate support to students by answering questions based exclusively on official course materials[cite: 16].

[cite_start]The system uses a modular strategy to efficiently combine local semantic analysis with a powerful generative AI model[cite: 37].

---

## ✨ Key Objectives and Features

The chatbot was designed with the following core objectives:

* [cite_start]**Customized and Correct Answers:** Provide relevant and accurate responses based only on official `.docx` course materials[cite: 16, 17].
* [cite_start]**Transparency (Source Citation):** Justify every answer by citing the exact source, including the module, topic, level, and estimated page number of the identified paragraph[cite: 17, 40, 59].
* [cite_start]**Efficiency and Cost Optimization:** Minimize resource consumption and API costs by determining the relevant context locally before calling the generative model[cite: 35, 37].
* [cite_start]**Scalability:** Allow for easy addition of other courses[cite: 18].
* [cite_start]**User Experience (UX):** Offer a beautiful and captivating web interface[cite: 16, 18, 57].

---

## 💻 Technical Implementation Details

[cite_start]The project implementation involved combining three important components: document processing, semantic content identification, and adaptive response generation[cite: 43]. [cite_start]The application is built using Python, leveraging the Flask framework for server management[cite: 44].

### 1. Retrieval-Augmented Generation (RAG) Strategy

[cite_start]The core strength of the solution lies in its efficient RAG strategy[cite: 37]:

* [cite_start]**Local Context Identification:** For every user question, the application transforms all available document paragraphs and the question into embedding vectors using the **`sentence-transformers`** package and the **`all-MiniLM-L6-v2`** model[cite: 27, 28, 51]. [cite_start]The paragraph with the highest cosine similarity is identified as the most relevant[cite: 38, 52].
* [cite_start]**Generative AI:** Only this single, most relevant fragment is then sent as a prompt context to **OpenAI GPT-3.5**, which formulates the final, clear, and detailed response[cite: 29, 39, 54, 56].

### 2. Document Processing

* [cite_start]**Format:** The system analyzes course documents structured in the `.docx` format[cite: 17, 31, 45].
* [cite_start]**Extraction:** The **`python-docx`** library is used to extract, process, and iterate through individual paragraphs[cite: 32, 47].
* [cite_start]**Metadata:** Each extracted paragraph is tagged with metadata, including the file name, paragraph index, and estimated page number[cite: 48].

### 3. Frontend & Interaction

* [cite_start]The web interface is developed using **HTML** and **CSS**, with **JavaScript** handling real-time interaction with the Flask server[cite: 58].
* [cite_start]The UI includes "typing" animations and quick suggestion buttons to enhance user interaction[cite: 60].

---

## 🛠️ Technology Stack

| Category | Technology | Purpose |
| :---: | :---: | :--- |
| **Backend Framework** | Python / Flask | [cite_start]Managing the web server and defining HTTP routes[cite: 44, 73]. |
| **Generative Model** | OpenAI GPT-3.5 | [cite_start]Generating coherent, natural language responses via API[cite: 29, 74]. |
| **Semantic Search** | Sentence Transformers | [cite_start]Local text vectorization and semantic comparison[cite: 27, 76]. |
| **Document Parsing** | `python-docx` | [cite_start]Extracting content from `.docx` files[cite: 75]. |
| **Dependency** | `torch` | [cite_start]Essential dependency for the embedding model[cite: 77]. |

---

## 🚀 Run Instructions

[cite_start]The system was developed in Python3 and uses standard open-source libraries[cite: 70].

### 1. Installation

[cite_start]It is recommended to use a virtual environment (`venv`)[cite: 81]. Install all required dependencies using `pip`:

```bash
pip install flask openai python-docx sentence-transformers torch
