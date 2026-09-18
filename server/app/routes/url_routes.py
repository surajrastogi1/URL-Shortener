from fastapi import APIRouter
from app.database.tables import URLCreate, URL
from app.services.url_services import create_short_url,get_long_url
from fastapi.responses import RedirectResponse
import os
from dotenv import load_dotenv
load_dotenv()

router = APIRouter()

BASE_URL = os.getenv("BASE_URL")

@router.post("/urls")
def create_url(data: URLCreate):
    url = create_short_url(str(data.long_url))

    return {
        "short_url" : (f"{BASE_URL}/{url.short_code}")
    }



@router.get("/{short_code}")
def get_url(short_code: str):
    url = get_long_url(short_code)

    return RedirectResponse(url=url.long_url)
