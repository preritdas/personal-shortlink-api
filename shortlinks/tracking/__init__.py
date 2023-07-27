"""Track link clicks with ipstack."""
import requests

from keys import KEYS


def ip_to_city(ip: str) -> str:
    """Get city from IP address."""
    url = f"http://api.ipstack.com/{ip}?access_key={KEYS.ipstack.api_key}"
    res = requests.get(url)
    res.raise_for_status()
    return res.json()["city"]
