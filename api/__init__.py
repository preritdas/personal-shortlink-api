"""API routers."""
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse

from shortlinks import find_shortlink
from shortlinks.tracking import track_click

from api.manage import router


app = FastAPI()

# Include manage router
app.include_router(router, prefix="/manage")


@app.get("/")
async def root_redirect():
    """If the user visits the root path, redirect them to the main website."""
    return RedirectResponse("https://preritdas.com")


@app.get("/{code}")
async def main_handler(code: str, request: Request):
    shortlink = find_shortlink(code)

    if not shortlink:
        return "Shortlink not found or shortlink expired."

    # Track the click
    track_click(
        ip=request.client.host,
        code=code
    )

    return RedirectResponse(shortlink)
