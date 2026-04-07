from transformers import pipeline
import torch
import logging
from utils.chunking import Chunker

logger = logging.getLogger(__name__)

class SummarizerAgent:
    def __init__(self):
        self.name = "Summarizer Agent"
        self.chunker = Chunker(max_chars=900)

        # Check device (GPU if available)
        device = 0 if torch.cuda.is_available() else -1
        logger.info(f"Loading model on {'GPU' if device == 0 else 'CPU'}")

        # Use lightweight stable model
        self.summarizer = pipeline(
            "summarization",
            model="sshleifer/distilbart-cnn-12-6",
            device=device
        )

    def run(self, text: str) -> str:
        if not text or len(text.strip()) < 50:
            return text

        logger.info("Starting summarization process...")

        chunks = self.chunker.chunk_text(text)
        summaries = []

        for i, chunk in enumerate(chunks):
            logger.info(f"Summarizing chunk {i+1}/{len(chunks)}")

            try:
                if len(chunk) < 50:
                    summaries.append(chunk)
                    continue

                result = self.summarizer(
                    chunk,
                    max_length=150,
                    min_length=40,
                    do_sample=False
                )

                summaries.append(result[0]['summary_text'])

            except Exception as e:
                logger.warning(f"Error in chunk {i}: {e}")
                summaries.append(chunk)

        final_summary = " ".join(summaries)

        logger.info("Summarization completed.")
        return final_summary