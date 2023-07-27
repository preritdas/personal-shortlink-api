"""Track link clicks with ipstack."""
import requests

from datetime import datetime

from keys import KEYS
from shortlinks.database import SHORTLINKS


def ip_to_city(ip: str) -> str:
    """Get city from IP address."""
    url = f"http://api.ipstack.com/{ip}?access_key={KEYS.ipstack.api_key}"
    res = requests.get(url)
    res.raise_for_status()
    return res.json()["city"]


def track_click(ip: str, code: str) -> None:
    """Track a click by adding the city and time to the shortlink's clicks."""
    city = ip_to_city(ip)
    SHORTLINKS.update_one(
        {"code": code},
        {"$push": {"clicks": {"city": city, "time": datetime.now()}}},
    )
