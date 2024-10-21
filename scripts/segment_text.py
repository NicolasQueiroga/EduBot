import os
import re


def segment_text(text, max_words=500):
    words = text.split()
    segments = []
    for i in range(0, len(words), max_words):
        segment = " ".join(words[i : i + max_words])
        segments.append(segment)
    return segments


def segment_texts(input_dir, output_dir, max_words=500):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for txt_file in os.listdir(input_dir):
        if txt_file.endswith(".txt"):
            txt_path = os.path.join(input_dir, txt_file)
            with open(txt_path, "r", encoding="utf-8") as f:
                text = f.read()

            segments = segment_text(text, max_words)
            base_filename = os.path.splitext(txt_file)[0]
            for idx, segment in enumerate(segments):
                segment_filename = f"{base_filename}_segment_{idx+1}.txt"
                segment_path = os.path.join(output_dir, segment_filename)
                with open(segment_path, "w", encoding="utf-8") as f:
                    f.write(segment)
            print(f"Segmented {txt_file} into {len(segments)} parts")


if __name__ == "__main__":
    cleaned_text_dir = "data/cleaned_texts"
    segmented_text_dir = "data/segmented_texts"
    segment_texts(cleaned_text_dir, segmented_text_dir, max_words=500)
