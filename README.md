# CHATBOT
# 🤖 AI Educational Chatbot: Personalized Learning Assistant

This project is an advanced educational chatbot developed at the Politehnica University of Bucharest, Faculty of Automation and Computer Science for the Algorithms Design course. Its main goal is to provide personalized and accurate support to students by answering questions based exclusively on official course materials.

The system uses a modular strategy to efficiently combine local semantic analysis with a powerful generative AI model.

---

## ✨ Key Objectives and Features

The chatbot was designed with the following core objectives:

* **Customized and Correct Answers:** Provide relevant and accurate responses based only on official `.docx` course materials.
* **Transparency (Source Citation):** Justify every answer by citing the exact source, including the module, topic, level, and estimated page number of the identified paragraph.
* **Efficiency and Cost Optimization:** Minimize resource consumption and API costs by determining the relevant context locally before calling the generative model.
* **Scalability:** Allow for easy addition of other courses.
* **User Experience (UX):** Offer a beautiful and captivating web interface.

---

## 💻 Technical Implementation Details

The project implementation involved combining three important components: document processing, semantic content identification, and adaptive response generation. The application is built using Python, leveraging the Flask framework for server management.

### 1. Retrieval-Augmented Generation (RAG) Strategy

The core strength of the solution lies in its efficient RAG strategy:

* **Local Context Identification:** For every user question, the application transforms all available document paragraphs and the question into embedding vectors using the **`sentence-transformers`** package and the **`all-MiniLM-L6-v2`** model. The paragraph with the highest cosine similarity is identified as the most relevant.
* **Generative AI:** Only this single, most relevant fragment is then sent as a prompt context to **OpenAI GPT-3.5**, which formulates the final, clear, and detailed response.

### 2. Document Processing

* **Format:** The system analyzes course documents structured in the `.docx` format.
* **Extraction:** The **`python-docx`** library is used to extract, process, and iterate through individual paragraphs.
* **Metadata:** Each extracted paragraph is tagged with metadata, including the file name, paragraph index, and estimated page number.

### 3. Frontend & Interaction

* The web interface is developed using **HTML** and **CSS**, with **JavaScript** handling real-time interaction with the Flask server.
* The UI includes "typing" animations and quick suggestion buttons to enhance user interaction.

---

## 🛠️ Technology Stack

| Category | Technology | Purpose |
| :---: | :---: | :--- |
| **Backend Framework** | Python / Flask | Managing the web server and defining HTTP routes. |
| **Generative Model** | OpenAI GPT-3.5 | Generating coherent, natural language responses via API. |
| **Semantic Search** | Sentence Transformers | Local text vectorization and semantic comparison. |
| **Document Parsing** | `python-docx` | Extracting content from `.docx` files. |
| **Dependency** | `torch` | Essential dependency for the embedding model. |

---

## 🚀 Run Instructions

The system was developed in Python3 and uses standard open-source libraries.

### 1. Installation

It is recommended to use a virtual environment (`venv`). Install all required dependencies using `pip`:

```bash
pip install flask openai python-docx sentence-transformers torch
