import os
import json
from elasticsearch import Elasticsearch, helpers


def create_index(es, index_name):
    if not es.indices.exists(index=index_name):
        es.indices.create(
            index=index_name,
            body={
                "settings": {"number_of_shards": 1, "number_of_replicas": 0},
                "mappings": {
                    "properties": {
                        "content": {"type": "text", "analyzer": "standard"},
                        "subject": {"type": "keyword"},
                        "topic": {"type": "keyword"},
                        "segment_id": {"type": "integer"},
                    }
                },
            },
        )
        print(f"Created index '{index_name}'")
    else:
        print(f"Index '{index_name}' already exists")


def generate_actions(segmented_dir, index_name):
    for txt_file in os.listdir(segmented_dir):
        if txt_file.endswith(".txt"):
            parts = txt_file.split("_segment_")
            base_filename = parts[0]
            segment_id = int(parts[1].split(".txt")[0])

            if "algebra" in base_filename.lower():
                subject = "mathematics"
                topic = "algebra"
            elif "calculus" in base_filename.lower():
                subject = "mathematics"
                topic = "calculus"
            elif "linear" in base_filename.lower():
                subject = "mathematics"
                topic = "linear algebra"
            elif "differential" in base_filename.lower():
                subject = "mathematics"
                topic = "differential equations"
            elif "mechanics" in base_filename.lower():
                subject = "physics"
                topic = "mechanics"
            elif "electromagnetism" in base_filename.lower():
                subject = "physics"
                topic = "electromagnetism"
            elif "thermodynamics" in base_filename.lower():
                subject = "physics"
                topic = "thermodynamics"
            elif "general" in base_filename.lower():
                subject = "chemistry"
                topic = "general chemistry"
            elif "organic" in base_filename.lower():
                subject = "chemistry"
                topic = "organic chemistry"
            elif "inorganic" in base_filename.lower():
                subject = "chemistry"
                topic = "inorganic chemistry"
            else:
                subject = "unknown"
                topic = "unknown"

            txt_path = os.path.join(segmented_dir, txt_file)
            with open(txt_path, "r", encoding="utf-8") as f:
                content = f.read()

            yield {
                "_index": index_name,
                "_source": {
                    "content": content,
                    "subject": subject,
                    "topic": topic,
                    "segment_id": segment_id,
                },
            }


def main():
    es = Elasticsearch("http://localhost:9200/")
    index_name = "edubot_knowledge_base"
    create_index(es, index_name)

    segmented_dir = "data/segmented_texts"
    actions = generate_actions(segmented_dir, index_name)

    helpers.bulk(es, actions)
    print("Indexed all segmented texts into Elasticsearch")


if __name__ == "__main__":
    main()
