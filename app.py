import streamlit as st
import os
from main import ResearchOrchestrator
from utils.memory import Memory

# Page Config
st.set_page_config(
    page_title="Multi-Agent Researcher",
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

# Cache orchestrator (prevents model reload)
@st.cache_resource
def load_orchestrator():
    return ResearchOrchestrator()

# Cache history
@st.cache_data
def get_history():
    mem = Memory()
    return mem.get_history()

# UI Header
st.markdown('<div class="main-header">Multi-Agent Researcher</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">AI-Powered Research, Filtering, and Reporting System</div>', unsafe_allow_html=True)

# Sidebar History
st.sidebar.title("📜 Search History")
history = get_history()

if history:
    for item in history:
        with st.sidebar.expander(f"{item['topic']} ({item['timestamp']})"):
            st.write(item['summary_preview'])
else:
    st.sidebar.write("No history found.")

# Main Input Area
col1, col2 = st.columns([4, 1])

with col1:
    topic_input = st.text_input(
        "Enter a topic to research:",
        placeholder="Type any topic for Research -> Download PDF"
    )

with col2:
    generate_btn = st.button("Generate Report", type="primary")

# Generate Report
if generate_btn:
    if not topic_input.strip():
        st.error("Please enter a topic.")
    else:
        with st.spinner("Agents are working... (Researching → Filtering → Summarizing → Writing)"):
            try:
                orchestrator = load_orchestrator()
                report, pdf_path = orchestrator.run_research_pipeline(topic_input)

                if report:
                    st.success("Report Generated Successfully!")

                    # 🔥 FIX: refresh history
                    st.cache_data.clear()

                    # Display Report
                    st.header(f"Report: {report['topic']}")

                    st.subheader("Introduction")
                    st.write(report['introduction'])

                    st.subheader("Key Insights")
                    st.write(report['key_insights'])

                    st.subheader("Conclusion")
                    st.write(report['conclusion'])

                    # Download PDF
                    if pdf_path and os.path.exists(pdf_path):
                        with open(pdf_path, "rb") as pdf_file:
                            st.download_button(
                                label="📄 Download PDF Report",
                                data=pdf_file,
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
