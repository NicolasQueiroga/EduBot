import os
from pdfminer.high_level import extract_text


def extract_texts(pdf_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for pdf_file in os.listdir(pdf_dir):
        if pdf_file.endswith(".pdf"):
            pdf_path = os.path.join(pdf_dir, pdf_file)
            text = extract_text(pdf_path)
            txt_filename = os.path.splitext(pdf_file)[0] + ".txt"
            txt_path = os.path.join(output_dir, txt_filename)
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"Extracted text from {pdf_file} to {txt_filename}")


if __name__ == "__main__":
    pdf_directory = "data/pdfs"
    text_output_directory = "data/texts"
    extract_texts(pdf_directory, text_output_directory)
