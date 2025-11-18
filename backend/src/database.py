from loguru import logger
from mongoengine import connect, disconnect

from src import extensions


def connect_database():
    try:
        db = extensions.settings.database.MONGO_DATABASE
        host = extensions.settings.database.MONGO_URI
        connect(host=host, db=db)
        logger.info(f"Connected to MongoDB successfully - Database: {db}")
    except Exception as e:
        logger.error(f"Failed to connect to MongoDB: {str(e)}")


def close_database():
    try:
        disconnect()
        logger.info(f"MongoDB connection closed")
    except Exception as e:
        logger.error(f"Failed to close MongoDB connection: {str(e)}")