# 🍕 Pizza Restaurant AI Assistant

**A smart RAG-powered AI chatbot** that answers any question about a pizza restaurant using **100+ real customer reviews**.

Built with **LangChain + Ollama + Chroma** and a beautiful web interface with **Streamlit**.

![Demo](https://img.shields.io/badge/Status-Live-brightgreen)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-orange)

---

### 🎥 Demo Video

**Watch how it works in action:**

[![Pizza AI Demo Video](https://img.youtube.com/vi/gglETHrn-pA/0.jpg)](https://youtu.be/gglETHrn-pA)


### ✨ Features

- ✅ Answers questions using real customer reviews (RAG)
- ✅ Beautiful modern chat interface (Streamlit)
- ✅ Runs 100% locally (no internet or API keys needed after setup)
- ✅ Two versions: Console + Web UI
- ✅ Smart retrieval of top 5 relevant reviews
- ✅ Supports questions about crust, service, vegan options, prices, best pizzas, etc.

---

### 🛠️ Tech Stack

- **Python 3.12**
- **LangChain** + **LangChain-Ollama**
- **Ollama** (llama3.2 + mxbai-embed-large)
- **Chroma** (Vector Database)
- **Streamlit** (Web Frontend)
- **Pandas** (Data handling)

---

### 📁 Project Structure

D:\Local_Agent/  
├── main.py                 # Original console version  
├── app.py                  # Beautiful Streamlit web version ← RECOMMENDED  
├── vector.py               # Creates vector database from reviews  
├── requirements.txt  
├── realistic_restaurant_reviews.csv  
├── chrome_langchain_db/    # Auto-created folder (do NOT delete)  
└── README.md  




### 🚀 Installation (Step-by-Step)

#### 1. Install Ollama
- Download from: https://ollama.com/download
- Install and open it once.

#### 2. Pull the models (run in Command Prompt)


ollama pull llama3.2
ollama pull mxbai-embed-large


3. Clone or download this repository
cmdcd /d D:\Local_Agent
4. Create environment & install packages
cmdpython -m venv transformer
transformer\Scripts\activate
pip install -r requirements.txt
pip install streamlit

▶️ How to Run
Option A: Beautiful Web Version (Recommended)
cmdcd /d D:\Local_Agent
transformer\Scripts\activate
streamlit run app.py
Option B: Console Version
cmdcd /d D:\Local_Agent
transformer\Scripts\activate
python main.py



Parts of this implementation are based on the following repository:
https://github.com/techwithtim/LocalAIAgentWithRAG/tree/main
