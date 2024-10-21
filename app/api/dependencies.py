from app.db.mongodb import db
from app.db.elasticsearch import es
from app.db.redis import redis_client as redis


def get_db():
    return db


def get_es():
    return es


def get_redis():
    return redis
