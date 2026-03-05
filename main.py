from fastapi import FastAPI
from pydantic import BaseModel
import random
import string

app = FastAPI()

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
    short_code = generate_short_code()
    url_store[short_code] = request.original_url

    return {
        "short_url": f"http://127.0.0.1:8000/{short_code}"
    }

@app.get("/{short_code}")
def redirect_url(short_code: str):
    if short_code in url_store:
        return {"original_url": url_store[short_code]}
    else:
        return {"error": "Short URL not found"}