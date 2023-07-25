"""CRUD operations for the links."""
from fastapi import APIRouter
from pydantic import BaseModel

from datetime import datetime

from shortlinks import create_shortlink


router = APIRouter()


class Link(BaseModel):
    """Link model."""
    code: str
    url: str
    expiration: datetime = None


@router.get("/create")
async def create(shortlink: Link):
    """Create a shortlink."""
    res = create_shortlink(shortlink.url, shortlink.code, shortlink.expiration)

    if res:
        return "Shortlink created successfully."

    return "Shortlink already exists."
