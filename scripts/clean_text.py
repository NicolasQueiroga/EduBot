import os
import re


def clean_texts(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for txt_file in os.listdir(input_dir):
        if txt_file.endswith(".txt"):
            txt_path = os.path.join(input_dir, txt_file)
            with open(txt_path, "r", encoding="utf-8") as f:
                text = f.read()

            text = re.sub(r"\s+", " ", text)
            text = re.sub(r"[^A-Za-z0-9.,!?;:\'\-\s]", "", text)

            cleaned_txt_path = os.path.join(output_dir, txt_file)
            with open(cleaned_txt_path, "w", encoding="utf-8") as f:
                f.write(text)

            print(f"Cleaned text for {txt_file}")


if __name__ == "__main__":
    raw_text_dir = "data/texts"
    cleaned_text_dir = "data/cleaned_texts"
    clean_texts(raw_text_dir, cleaned_text_dir)
