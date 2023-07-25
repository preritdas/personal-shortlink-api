"""API routers."""
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from shortlinks import find_shortlink

from api.manage import router


app = FastAPI()

# Include manage router
app.include_router(router, prefix="/manage")


@app.get("/")
async def root_redirect():
    """If the user visits the root path, redirect them to the main website."""
    return RedirectResponse("https://preritdas.com")


@app.get("/{code}")
async def main_handler(code: str):
    shortlink = find_shortlink(code)

    if not shortlink:
        return "Shortlink not found or shortlink expired."

    return RedirectResponse(shortlink)
