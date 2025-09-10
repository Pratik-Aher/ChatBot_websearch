# 🤖 Groq RAG Chatbot  

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)  
[![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-brightgreen)](https://streamlit.io/cloud)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  

An intelligent chatbot built with **Streamlit** and **Groq LLM** that combines **document-based Q&A (RAG)** and **real-time web search** for contextual, accurate, and flexible conversations.  

---

## 🚀 Use Case Objective
- Enable users to **chat with their documents** (PDF, TXT, DOCX).  
- Provide **real-time web answers** when local knowledge is insufficient.  
- Allow flexible **Concise / Detailed** response modes.  

---

## 🛠️ Features
✅ **RAG Integration** – Upload documents and query them with embeddings.  
✅ **Live Web Search** – Uses Tavily API for real-time search.  
✅ **Concise vs Detailed Responses** – Choose the style of answers.  
✅ **Clear Chat History** – Reset anytime from the sidebar.  
✅ **Modular Design** – Easy to extend with new tools & providers.  

---

## 📂 Project Structure
```
groq-rag-chatbot/
├── app.py                  # Main Streamlit app
├── config/
│   └── config.py           # API key loading (env variables / dotenv)
├── models/
│   └── llm.py              # Groq LLM integration
├── utils/
│   ├── rag.py              # Retrieval-Augmented Generation logic
│   ├── web_search.py       # Live web search with Tavily
│   ├── vectorstore.py      # Vector DB management (FAISS)
│   ├── doc_loader.py       # PDF/TXT file loaders
│   ├── prompting.py        # Prompt templates
│   └── logger.py           # Error logging
├── requirements.txt        # Dependencies
└── README.md               # Project documentation
```

---

## ⚡ Installation

### 1. Clone Repo
```bash
git clone https://github.com/your-username/groq-rag-chatbot.git
cd groq-rag-chatbot
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set API Keys
Create a `.env` file in the project root:  
```
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

Alternatively, export them in your shell:
```bash
export GROQ_API_KEY="your_groq_api_key"
export TAVILY_API_KEY="your_tavily_api_key"
```

---

## ▶️ Running the App
```bash
streamlit run app.py
```

- Local URL: [http://localhost:8501](http://localhost:8501)  
- Network URL: (shown in terminal)  

---

## 🌐 Deployment (Streamlit Cloud)
1. Push this repo to GitHub.  
2. Go to [Streamlit Cloud](https://streamlit.io/cloud).  
3. Create a new app → Select your repo → Choose `app.py` as the main file.  
4. Add your secrets in **Streamlit Cloud → Settings → Secrets**:
   ```toml
   GROQ_API_KEY="your_groq_api_key"
   TAVILY_API_KEY="your_tavily_api_key"
   ```

---

## 📜 License
MIT License © 2025 [Pratik Aher]  
