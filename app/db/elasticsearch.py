from elasticsearch import Elasticsearch
from app.core.config import settings
from app.core.logger import logger

try:
    es = Elasticsearch(settings.ELASTICSEARCH_HOST)
    if es.ping():
        logger.info("Connected to Elasticsearch successfully.")
    else:
        logger.error("Elasticsearch ping failed.")
except Exception as e:
    logger.error(f"Failed to connect to Elasticsearch: {e}")
    raise e
