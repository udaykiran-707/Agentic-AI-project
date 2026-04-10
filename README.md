🚀 MULTI AGENT RESEARCHER & REPORT GENERATOR

An AI-powered multi-agent system that automates the complete research workflow — from data collection to structured report generation and PDF export.

---

🔁 Agentic Workflow

User Input → Research Agent → Filter Agent → Summarizer Agent → Writer Agent → PDF + UI Output

---

1. Business Problem

In today’s digital age, research is inefficient due to:

- Information overload from multiple sources
- Lack of a unified system to aggregate data
- Difficulty in summarizing large content
- Time-consuming report formatting

---

2. Possible Solution

- Use Agentic Workflow (Researcher, Filter, Summarizer, Writer)
- Apply NLP Models (BART/T5) for summarization
- Use Web APIs (Wikipedia, DuckDuckGo) for data collection
- Generate reports dynamically using PDF libraries

---

3. Implemented Solution

A fully functional Multi-Agent Research System built in Python.

🔁 Workflow:

- 🔍 Research Agent → Collects data from Wikipedia & web
- 🧹 Filter Agent → Cleans unwanted data
- 🧠 Summarizer Agent → Uses BART model for summarization
- 📄 Writer Agent → Creates structured report
- 📥 PDF Generator → Generates downloadable report
- 💾 Memory → Stores history in JSON

---

⚙️ How It Works

1. User enters a topic
2. System collects and processes data using agents
3. Generates structured report
4. Converts it into downloadable PDF
5. Stores history for future use

---

✨ Features

- Multi-agent architecture
- Real-time agent execution visualization
- Automated research → filtering → reporting pipeline
- PDF report generation
- Memory-based history tracking
- Interactive Streamlit UI
- Deployed and accessible online

---

4. Tech Stack Used

- Python → Core logic and backend development  
- Streamlit → User interface and interaction  
- HuggingFace Transformers → Text summarization  
- PyTorch → Backend for AI models  
- Wikipedia API → Fetching encyclopedia data  
- DuckDuckGo Search → Fetching web data  
- FPDF → Generating PDF reports  
- requests, re, json → Data processing and utilities

---

5. Architecture Diagram

User → Streamlit UI → Orchestrator
        ↓
   Research Agent
        ↓
   Filter Agent
        ↓
   Chunker
        ↓
   Summarizer Agent
        ↓
   Writer Agent
        ↓
   PDF Generator → Download
        ↓
   Memory (JSON Storage)

---

📂 Project Structure

My_Agent_Project/
│
├── agents/
│   ├── research.py
│   ├── filter.py
│   ├── writer.py
│   ├── summarizer.py
│
├── utils/
│   └── memory.py
│
├── app.py
├── main.py
├── requirements.txt
└── outputs/

---

6. How to Run in Local

Prerequisites

- Python 3.8+
- pip

Steps

git clone "https://github.com/your-username/your-repo-name.git" (https://github.com/your-username/your-repo-name.git)
cd your-repo-name

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

streamlit run app.py

---

🌐 Live Demo

👉 "https://agentic-multi-agents.streamlit.app/" (https://agentic-multi-agents.streamlit.app/)

---

💻 GitHub Repository

👉 "https://github.com/udaykiran-707/Agentic-AI-project" (https://github.com/udaykiran-707/Agentic-AI-project)

---

7. References and Resources Used

- HuggingFace Transformers
- Facebook BART Model
- Wikipedia API
- DuckDuckGo Search
- Streamlit Documentation
- FPDF Documentation

---

8. Recording

 



---

9. Screenshots

- Home Screen
 <img width="1920" height="1080" alt="Screenshot 2026-04-09 160257" src="https://github.com/user-attachments/assets/6d14a355-3045-4db6-a72c-3c5855b97a7e" />

- Agent Workflow
 <img width="1920" height="1080" alt="Screenshot 2026-04-09 161251" src="https://github.com/user-attachments/assets/f34a8c55-bb54-4630-a77e-128eee59889b" />

- Generated Report
  <img width="1920" height="1080" alt="Screenshot 2026-04-09 161306" src="https://github.com/user-attachments/assets/a90611ee-56a4-446e-bcaf-38e42edc620b" />

- PDF Download
  <img width="1920" height="1080" alt="Screenshot 2026-04-09 161626" src="https://github.com/user-attachments/assets/1b5e35cc-584f-4a27-ac29-cff249e9417b" />

  

---

10. Problems Faced and Solutions

- Token limit errors → Implemented chunking to handle large text inputs  
- API costs → Used DuckDuckGo search to avoid paid APIs  
- Wikipedia ambiguity → Added error handling for disambiguation issues  
- PDF encoding issues → Cleaned text to remove unsupported characters  
- Slow UI → Used caching and Streamlit spinner for better performance

---

🎯 What I Learned

- Designing multi-agent workflows
- Breaking complex systems into modular components
- Building real-world AI applications
- Deploying applications

---

🔮 Future Improvements

- Add advanced AI/LLM summarization
- Improve UI/UX with animations
- Add database for persistent storage
- Integrate more data sources

---

🤝 Contributing

Contributions are welcome! Feel free to fork this repo and submit a pull request.

---

📜 License

MIT License

---

👨‍💻 Author

K Uday Kiran Achari - Agentic AI

---

⭐ If you like this project, give it a star!
