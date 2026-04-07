import logging

logger = logging.getLogger(__name__)

class Chunker:
    def __init__(self, max_chars=1000):
        self.max_chars = max_chars

    def chunk_text(self, text: str) -> list:
        """
        Splits text into chunks. 
        Tries to split by paragraphs first, then sentences if needed.
        """
        if len(text) <= self.max_chars:
            return [text]
        
        chunks = []
        current_chunk = ""
        
        # Split by double newlines (paragraphs)
        paragraphs = text.split('\n\n')
        
        for paragraph in paragraphs:
            # If a single paragraph is too long, split by sentence
            if len(paragraph) > self.max_chars:
                sentences = paragraph.split('. ')
                for sentence in sentences:
                    sentence += ". " # Add period back
                    if len(current_chunk) + len(sentence) <= self.max_chars:
                        current_chunk += sentence
                    else:
                        if current_chunk:
                            chunks.append(current_chunk.strip())
                        current_chunk = sentence
            else:
                # Check if adding paragraph exceeds limit
                if len(current_chunk) + len(paragraph) <= self.max_chars:
                    current_chunk += paragraph + "\n\n"
                else:
                    if current_chunk:
                        chunks.append(current_chunk.strip())
                    current_chunk = paragraph + "\n\n"
        
        # Add remaining
        if current_chunk:
            chunks.append(current_chunk.strip())
            
        logger.info(f"Split text into {len(chunks)} chunks.")
        return chunks