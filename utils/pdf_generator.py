from fpdf import FPDF
import os
import logging
import re

logger = logging.getLogger(__name__)

class PDFGenerator:
    def __init__(self):
        self.name = "PDF Generator"

    # 🔥 FIX: clean text for FPDF
    def clean_text(self, text: str) -> str:
        return text.encode('latin-1', 'ignore').decode('latin-1')

    def generate(self, report: dict) -> str:
        logger.info("Generating PDF...")
        
        pdf = FPDF()
        pdf.add_page()
        
        # Title
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(200, 10, txt=self.clean_text(f"Research Report: {report['topic']}"), ln=True, align='C')
        pdf.ln(10)
        
        # Introduction
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(200, 10, txt="Introduction", ln=True)
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, txt=self.clean_text(report['introduction']))
        pdf.ln(5)
        
        # Key Insights
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(200, 10, txt="Key Insights (AI Summarized)", ln=True)
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, txt=self.clean_text(report['key_insights']))
        pdf.ln(5)
        
        # Conclusion
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(200, 10, txt="Conclusion", ln=True)
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, txt=self.clean_text(report['conclusion']))
        
        # Ensure output directory exists
        if not os.path.exists("outputs"):
            os.makedirs("outputs")

        # Safe filename
        safe_topic = re.sub(r'[^a-zA-Z0-9_]', '_', report['topic'])
        filename = f"outputs/report_{safe_topic}.pdf"

        pdf.output(filename)
        
        logger.info(f"PDF saved to {filename}")
        return filename