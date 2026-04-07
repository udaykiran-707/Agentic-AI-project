# 🤖 Multi-Agent Research Assistant

## 📌 Overview

The **Multi-Agent Research Assistant** is an AI-powered system designed to automate the process of researching, filtering, summarizing, and generating structured reports from multiple data sources.

This project follows an **agentic workflow**, where multiple specialized agents collaborate to solve a real-world problem: reducing the time and effort required for manual research and report creation.

---

## 🎯 Problem Statement

Students and professionals spend a significant amount of time searching, cleaning, and summarizing information from different sources.

This system addresses that problem by:

* Automatically collecting data
* Cleaning and filtering information
* Generating AI-based summaries
* Producing structured reports

---

## 🧠 Key Features

* 🔍 Multi-source data collection (Wikipedia + Web Search)
* 🧹 Intelligent data filtering and cleaning
* 🤖 AI-based summarization using Transformers
* 📝 Structured report generation
* 💾 Persistent memory (search history)
* 📄 PDF report export
* 🌐 Interactive web UI using Streamlit

---

## ⚙️ Tech Stack

* Python
* Streamlit
* Hugging Face Transformers
* PyTorch
* Wikipedia API
* DuckDuckGo Search
* FPDF

---

## 🤖 Agents Used

| Agent            | Role                                |
| ---------------- | ----------------------------------- |
| Research Agent   | Collects data from multiple sources |
| Filter Agent     | Cleans and processes raw data       |
| Summarizer Agent | Generates AI-based summaries        |
| Writer Agent     | Creates structured reports          |

---

## 🔁 Agentic Workflow

User Input → Research Agent → Filter Agent → Summarizer Agent → Writer Agent → PDF + UI Output

---

## 💾 Memory & Persistence

* Stores search history in `memory.json`
* Enables retrieval of past queries
* Provides summary preview in UI

---

## ⚠️ Guardrails

* Prevents empty input
* Handles errors gracefully
* Ensures system stability

---

## 📁 Project Structure

multi_agent_researcher/
│
├── agents/
│   ├── research.py
│   ├── filter.py
│   ├── summarizer.py
│   └── writer.py
│
├── utils/
│   ├── memory.py
│   ├── pdf_generator.py
│   └── chunking.py
│
├── data/
│   └── memory.json
│
├── outputs/
│   └── (generated PDFs)
│
├── main.py
├── app.py
├── requirements.txt
└── README.md

---

## ▶️ How to Run

1. Clone the repository
   git clone 
   cd multi_agent_researcher

2. Create virtual environment
   python -m venv venv
   venv\Scripts\activate

3. Install dependencies
   pip install -r requirements.txt

4. Run the application
   streamlit run app.py

---

## 🧪 Example Use Cases

* Research topics for assignments
* Quick knowledge summaries
* Report generation for presentations
* Learning new topics efficiently

---

## 🌐 Deployment

This project can be deployed using:

* Hugging Face Spaces
* Streamlit Cloud

---

## 🚀 Future Enhancements

* Integration with Vector Databases
* Semantic search capabilities
* Multi-language support
* Voice input support

---

## 📊 Demo

* Enter a topic
* Generate report
* Download PDF
* View history

---

## 📌 Conclusion

This project demonstrates how **multi-agent systems** can automate complex workflows like research and report generation using AI.

---

## 👨‍💻 Author

Uday Kiran
