from pymongo import MongoClient
from app.core.config import settings
from app.core.logger import logger

try:
    client = MongoClient(settings.MONGO_URI)
    db = client.edubot
    logger.info("Connected to MongoDB successfully.")
except Exception as e:
    logger.error(f"Failed to connect to MongoDB: {e}")
    raise e
