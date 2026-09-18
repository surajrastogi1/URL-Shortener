import string
import secrets
from app.database.connection import SessionLocal
from app.database.tables import URL
from fastapi import HTTPException


def generate_short_code(length = 6):
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))


def create_short_url(long_url):
    db = SessionLocal()

    while True:
        short_code = generate_short_code()

        existing_url = db.query(URL).filter(
            URL.short_code == short_code
        ).first()

        if not existing_url:
            break

    new_url = URL(
        long_url = long_url,
        short_code=short_code
    )

    db.add(new_url)
    db.commit()
    db.refresh(new_url)

    db.close()

    return new_url

def get_long_url(short_code):
    db = SessionLocal()

    url = db.query(URL).filter(
        URL.short_code == short_code
    ).first()

    if not url:
        raise HTTPException(
            status_code=404,
            detail="Short URL not found"
        )

    return url


