import logging

logger = logging.getLogger(__name__)

class WriterAgent:
    def __init__(self):
        self.name = "Writer Agent"

    def run(self, topic: str, filtered_data: str, summary: str) -> dict:
        """Generates a structured report dictionary."""
        logger.info("Writing final report...")
        
        report = {
            "topic": topic,
            "introduction": f"This report provides a detailed analysis and research summary on the topic of '{topic}'. The data has been aggregated from multiple sources including Wikipedia and web search results, filtered for relevance, and processed by an AI summarization model.",
            "key_insights": summary, # The main summarized content
            "raw_details": filtered_data[:1000] + "..." if len(filtered_data) > 1000 else filtered_data, # Truncated for context
            "conclusion": f"In conclusion, '{topic}' is a multifaceted subject with significant information available across public domains. The summary above captures the essential points derived from the research agents."
        }
        
        logger.info("Report generation completed.")
        return report