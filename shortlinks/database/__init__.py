"""Database connection."""
from pymongo.mongo_client import MongoClient

from keys import KEYS


MONGO_CLIENT = MongoClient(KEYS.MongoDB.connect_str)
DATABASE = MONGO_CLIENT["Shortlinks"]


# Collections
SHORTLINKS = DATABASE["shortlinks"]
