import logging
import sys

from agents.research import ResearchAgent
from agents.filter import FilterAgent
from agents.summarizer import SummarizerAgent
from agents.writer import WriterAgent
from utils.memory import Memory
from utils.pdf_generator import PDFGenerator

# Configure Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

class ResearchOrchestrator:
    def __init__(self):
        self.research_agent = ResearchAgent()
        self.filter_agent = FilterAgent()
        self.summarizer_agent = SummarizerAgent()
        self.writer_agent = WriterAgent()
        self.memory = Memory()
        self.pdf_gen = PDFGenerator()

    def run_research_pipeline(self, topic: str):
        """Executes the full workflow."""
        if not topic or len(topic.strip()) == 0:
            raise ValueError("Topic cannot be empty.")

        print(f"\n=== Starting Research Pipeline for: {topic} ===\n")

        # Stage 1: Research
        try:
            raw_data = self.research_agent.run(topic)
        except Exception as e:
            logging.error(f"Research failed: {e}")
            return None, None

        # Stage 2: Filter
        try:
            clean_data = self.filter_agent.run(raw_data)
        except Exception as e:
            logging.error(f"Filtering failed: {e}")
            return None, None

        # Stage 3: Summarize
        try:
            summary = self.summarizer_agent.run(clean_data)
        except Exception as e:
            logging.error(f"Summarization failed: {e}")
            return None, None

        # Stage 4: Write
        try:
            report = self.writer_agent.run(topic, clean_data, summary)
        except Exception as e:
            logging.error(f"Writing failed: {e}")
            return None, None

        # Stage 5: Memory & PDF
        try:
            self.memory.save_search(topic, report)
            pdf_path = self.pdf_gen.generate(report)
        except Exception as e:
            logging.error(f"Saving or PDF generation failed: {e}")
            return report, None

        print("\n=== Pipeline Completed Successfully ===\n")
        return report, pdf_path


if __name__ == "__main__":
    orchestrator = ResearchOrchestrator()

    # ✅ user input (better than fixed topic)
    topic = input("Enter topic: ")

    report, pdf = orchestrator.run_research_pipeline(topic)

    if report:
        print("\n--- SUMMARY ---\n")
        print(report["key_insights"])

        if pdf:
            print("\nPDF saved at:", pdf)
        else:
            print("\nPDF generation failed.")
    else:
        print("\nPipeline failed. Check logs.")