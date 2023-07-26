"""Shortlink creation."""
from datetime import datetime

from shortlinks.database import SHORTLINKS
from shortlinks.database.checks import code_exists, code_expired


def find_shortlink(code: str) -> str:
    """
    Find a shortlink. Returns the URL. If it doesn't exist or if it exists 
    but is expired, return an empty string.
    """
    item = SHORTLINKS.find_one({"code": code, "expiration": {"$gte": datetime.now()}})

    if item:
        return item["url"]
    
    return ""


def create_shortlink(url: str, code: str, expiration: datetime = None) -> bool:
    """Create a shortlink. Returns False if the chosen code exists."""
    if find_shortlink(code):  # if a non-expired shortlink already exists
        return False

    SHORTLINKS.insert_one({"url": url, "code": code, "expiration": expiration})
    return True


def delete_shortlink(code: str) -> bool:
    """Delete a shortlink. Returns False if the shortlink doesn't exist."""
    if not code_exists(code):
        return False

    SHORTLINKS.delete_one({"code": code})
    return True
