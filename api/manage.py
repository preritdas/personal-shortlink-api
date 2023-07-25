"""CRUD operations for the links."""
from fastapi import APIRouter
from pydantic import BaseModel, Field, validator

from datetime import datetime

from shortlinks import create_shortlink, delete_shortlink


router = APIRouter()


class Link(BaseModel):
    """Link model."""
    code: str
    url: str
    expiration: str = Field("", description="Expiration date and time in YYYY-MM-DD format.")

    @validator("expiration")
    def expiration_datetime(cls, v):
        """Validate expiration."""
        if v:
            return datetime.strptime(v, "%Y-%m-%d")

        return v


class Code(BaseModel):
    """Code model."""
    code: str


@router.post("/create")
async def create(shortlink: Link):
    """Create a shortlink."""
    res = create_shortlink(shortlink.url, shortlink.code, shortlink.expiration)

    if res:
        return "Shortlink created successfully."

    return "Shortlink already exists."


@router.post("/delete")
async def delete(shortlink: Link):
    """Delete a shortlink."""
    res = delete_shortlink(shortlink.code)

    if res:
        return "Shortlink deleted successfully."

    return "Shortlink doesn't exist."
