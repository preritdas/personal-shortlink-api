"""API routers."""
from fastapi import FastAPI
from fastapi.responses import RedirectResponse


app = FastAPI()


@app.get("/")
async def root_redirect():
    """If the user visits the root path, redirect them to the main website."""
    return RedirectResponse("https://preritdas.com")
