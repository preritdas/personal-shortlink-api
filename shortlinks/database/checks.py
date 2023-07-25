"""Check for existing items in the database or expirations."""
from datetime import datetime

from database import SHORTLINKS


def code_exists(code: str) -> bool:
    """Check if a code exists in the database."""
    return bool(SHORTLINKS.find_one({"code": code}))


def code_expired(code: str) -> bool:
    """Check if a code has expired. Assumes the code exists."""
    item = SHORTLINKS.find_one({"code": code})
    return datetime.now() > item["expiration"]
