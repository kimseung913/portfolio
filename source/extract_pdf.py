import sys
from pypdf import PdfReader

def extract(pdf_path, out_path):
    with open(pdf_path, 'rb') as f:
        reader = PdfReader(f)
        text = ""
        for i, page in enumerate(reader.pages):
            text += f"\n--- Page {i+1} ---\n"
            text += page.extract_text() + "\n"
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(text)

extract("김승규_포트폴리오_지원.pdf", "old_portfolio.txt")
extract("투입인력 프로파일_V1_김승규책임.pdf", "new_profile.txt")
