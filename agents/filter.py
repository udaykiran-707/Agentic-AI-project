import re
import logging

logger = logging.getLogger(__name__)

class FilterAgent:
    def __init__(self):
        self.name = "Filter Agent"

    def clean_text(self, text: str) -> str:
        """Removes unnecessary characters, multiple spaces, and weird formatting."""
        if not text:
            return ""
            
        # Remove reference markers like [1], [20] common in Wikipedia
        text = re.sub(r'\[\d+\]', '', text)
        
        # Remove URLs
        text = re.sub(r'http\S+', '', text)
        
        # Remove extra whitespace/newlines
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text

    def extract_meaningful_segments(self, text: str) -> list:
        """Splits text into sentences and filters out very short ones."""
        if not text:
            return []

        # Simple sentence splitter
        sentences = re.split(r'(?<=[.!?]) +', text)
        
        meaningful = []
        for sent in sentences:
            clean_sent = sent.strip()
            # Filter out very short sentences or fragments
            if len(clean_sent) > 30: 
                meaningful.append(clean_sent)
        
        return meaningful

    def run(self, raw_data: str) -> str:
        """Filters and cleans the raw research data."""
        logger.info("Filtering and cleaning data...")
        
        # Remove separator used in research step
        parts = raw_data.split("---SOURCE_SEPARATOR---")
        cleaned_parts = []
        
        for part in parts:
            clean_part = self.clean_text(part)
            segments = self.extract_meaningful_segments(clean_part)
            cleaned_parts.append(" ".join(segments))
            
        result = "\n\n".join(cleaned_parts)
        logger.info("Filtering completed.")
        return result