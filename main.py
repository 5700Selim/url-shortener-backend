from fastapi import FastAPI
from pydantic import BaseModel
import random
import string
from fastapi.responses import RedirectResponse
from database import engine, Base
from database import SessionLocal
from models import URL
from services.cache import LRUCache

app = FastAPI()

Base.metadata.create_all(bind=engine)

cache = LRUCache(capacity=100)

# Temporary in-memory storage
url_store = {}

# Request model
class URLRequest(BaseModel):
    original_url: str

# Function to generate short code
def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

@app.post("/shorten")
def shorten_url(request: URLRequest):

    db = SessionLocal()

    short_code = generate_short_code()

    new_url = URL(
        short_code=short_code,
        original_url=request.original_url
    )

    db.add(new_url)
    db.commit()

    return {
        "short_url": f"http://127.0.0.1:8000/{short_code}"
    }

@app.get("/{short_code}")
def redirect_url(short_code: str):

    cached_url = cache.get(short_code)

    if cached_url:
        return RedirectResponse(cached_url)

    db = SessionLocal()

    url = db.query(URL).filter(URL.short_code == short_code).first()

    if url:
        cache.put(short_code, url.original_url)

        return RedirectResponse(url.original_url)

    return {"error": "Short URL not found"}