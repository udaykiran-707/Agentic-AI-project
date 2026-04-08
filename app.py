import streamlit as st
import os
import time
from main import ResearchOrchestrator
from utils.memory import Memory

# Page Config
st.set_page_config(
    page_title="Multi-Agent Researcher & Report Generator",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {font-size: 3rem; font-weight: bold; color: #4A90E2;}
    .sub-header {font-size: 1.2rem; color: #666;}
    </style>
""", unsafe_allow_html=True)

# Cache orchestrator
@st.cache_resource
def load_orchestrator():
    return ResearchOrchestrator()

# Cache history
@st.cache_data
def get_history():
    mem = Memory()
    return mem.get_history()

# Header
st.markdown('<div class="main-header">Multi-Agent Researcher & Report Generator</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">AI-Powered Research, Filtering, and Reporting System</div>', unsafe_allow_html=True)

# Sidebar History
st.sidebar.title("📜 Your History")
history = get_history()

if history:
    for item in history:
        with st.sidebar.expander(f"{item['topic']} ({item['timestamp']})"):
            st.write(item['summary_preview'])
else:
    st.sidebar.write("No history found.")

# Input UI
col1, col2 = st.columns([4, 1])

with col1:
    topic_input = st.text_input(
        "Enter a topic to research:",
        placeholder="Type any topic for Research → Download PDF"
    )

with col2:
    generate_btn = st.button("Generate Report", type="primary")

# 🔥 MAIN LOGIC WITH FLOW ANIMATION

if generate_btn:
    if not topic_input.strip():
        st.error("Please enter a topic.")
    else:
        flow = st.empty()

        try:
            orchestrator = load_orchestrator()
            steps = []

            # Step 1
            steps.append("🔍 Agent researching")
            flow.markdown(" → ".join(steps))
            time.sleep(1)
            raw_data = orchestrator.research_agent.run(topic_input)

            # Step 2
            steps.append("🧹 Agent filtering")
            flow.markdown(" → ".join(steps))
            time.sleep(1)
            clean_data = orchestrator.filter_agent.run(raw_data)

            # Step 3
            steps.append("🧠 Agent summarizing")
            flow.markdown(" → ".join(steps))
            time.sleep(1)
            summary = clean_data

            # Step 4
            steps.append("📄 Agent generating PDF")
            flow.markdown(" → ".join(steps))
            time.sleep(1)
            report = orchestrator.writer_agent.run(topic_input, clean_data, summary)
            pdf_path = orchestrator.pdf_gen.generate(report)

            # Save memory
            orchestrator.memory.save_search(topic_input, report)

            # Final flow success
            flow.success("🚀 All agents have successfully processed your request. Your report is ready!")

            # Refresh history
            st.cache_data.clear()

            # 📊 Show Report AFTER animation
            st.header(f"Report: {report['topic']}")

            st.subheader("Introduction")
            st.write(report['introduction'])

            st.subheader("Key Insights")
            st.write(report['key_insights'])

            st.subheader("Conclusion")
            st.write(report['conclusion'])

            # 📥 Download PDF
            if pdf_path and os.path.exists(pdf_path):
                with open(pdf_path, "rb") as pdf_file:
                    st.download_button(
                        "📄 Download Your PDF Report",
                        pdf_file,
                        file_name=os.path.basename(pdf_path),
                        mime="application/pdf"
                    )
            else:
                st.warning("PDF not available.")

        except ValueError as ve:
            st.error(f"Input Error: {ve}")
        except Exception as e:
            st.error(f"Unexpected error: {e}")
            st.info("Try another topic or check logs.")