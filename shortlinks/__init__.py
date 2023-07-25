"""Shortlink creation."""
from datetime import datetime

from database import SHORTLINKS
from database.checks import code_exists, code_expired


def create_shortlink(url: str, code: str, expiration: datetime = None) -> bool:
    """Create a shortlink. Returns False if the chosen code exists."""
    if code_exists(code):
        return False

    SHORTLINKS.insert_one({"url": url, "code": code, "expiration": expiration})
    return True


def find_shortlink(code: str) -> str:
    """
    Find a shortlink. Returns the URL. If it doesn't exist or if it exists 
    but is expired, return an empty string.
    """
    item = SHORTLINKS.find_one({"code": code})

    if item and not code_expired(code):
        return item["url"]

    return ""
