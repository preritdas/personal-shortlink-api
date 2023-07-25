"""API routers."""
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from shortlinks import find_shortlink


app = FastAPI()


@app.get("/{code}")
async def main_handler(code: str):
    """If the user visits the root path, redirect them to the main website."""
    shortlink = find_shortlink(code)

    if not shortlink:
        return "Shortlink not found or shortlink expired."

    return RedirectResponse(shortlink)
