import pdfplumber
import os

files = {
    "Reading Literature/chamberlain_microdystrophin_2023.pdf": "Reading Literature/text/chamberlain_microdystrophin_2023.txt",
    "Reading Literature/wang_aav_delivery_2024.pdf": "Reading Literature/text/wang_aav_delivery_2024.txt",
    "Reading Literature/walkey_aav_tropism_2025.pdf": "Reading Literature/text/walkey_aav_tropism_2025.txt",
    "Reading Literature/lomash_aav_regulatory_2025.pdf": "Reading Literature/text/lomash_aav_regulatory_2025.txt",
    "Reading Literature/brooks_platform_vector_2020.pdf": "Reading Literature/text/brooks_platform_vector_2020.txt",
}

os.makedirs("Reading Literature/text", exist_ok=True)

for pdf_path, txt_path in files.items():
    if not os.path.exists(pdf_path):
        print(f"MISSING: {pdf_path}")
        continue
    with pdfplumber.open(pdf_path) as pdf:
        text = "\n".join(page.extract_text() or "" for page in pdf.pages)
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Done: {txt_path}")
