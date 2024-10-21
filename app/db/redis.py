import redis
from app.core.config import settings
from app.core.logger import logger

try:
    redis_client = redis.Redis(host="redis", port=6379, db=0)
    redis_client.ping()
    logger.info("Connected to Redis successfully.")
except Exception as e:
    logger.error(f"Failed to connect to Redis: {e}")
    redis_client = None
    raise e
