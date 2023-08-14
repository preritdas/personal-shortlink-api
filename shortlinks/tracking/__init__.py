"""Track link clicks with ipstack."""
import requests

from datetime import datetime

from keys import KEYS
from shortlinks.database import SHORTLINKS


def ip_to_city(ip: str) -> str:
    """
    Get city and region, formatted, from IP address. Ex City, Region.
    If city is not found, return the IP address.
    """
    try:
        res = requests.get(
            f"https://api.apilayer.com/ip_to_location/{ip}",
            headers={
                "apikey": KEYS.APILayer.api_key
            }
        )
        res_json = res.json()
        city, region = res_json["city"], res_json["region_name"]
        return f"{city}, {region}"
    except (KeyError, requests.exceptions.RequestException):
        return ip


def track_click(ip: str, code: str) -> None:
    """Track a click by adding the city and time to the shortlink's clicks."""
    city = ip_to_city(ip)
    SHORTLINKS.update_one(
        {"code": code},
        {"$push": {"clicks": {"city": city, "time": datetime.now()}}},
    )
