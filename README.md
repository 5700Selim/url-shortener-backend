**URL SHORTENER PROJECT**

*Project Overview:* This is a URL Shortener Project built using **FastAPI**. It generates Short URL using **Base62 encoding**, implements **LRU caching** for faster redirection and uses **SQLAlchemy ORM** for database management.

*Features:*
- Generates short url from long url.
- Base62 encoding using database auto increment ID.
- LRU cache implementation for faster lookup.
- Manage database operation using SQLAlchemy.
- URL redirecting API.

*Tech Stack*
- Python
- FastAPI
- SQLAlchemy
- SQLite (default database)
- LRU cache system
- Base62 encoding

*Working*
1. URL shortening
   - User sends original URL.
   - The URL is stored in database.
   - Databse auto-generated ID is encoded using Base62 encoding.
   - Short code is mapped to the original URL.
  
2. Base62 encoding
   - Converts numeric ID to user friendly short string.
   - Uses 62 charactes (a-z, A_Z, 0-9).
  
3. LRU cache optimization
   - Frequently used URLs are stored in cache.
   - Reduce database overhead for repeated requests.
  
*Runing the server:* uvicorn main:app --reload

*Future improvements*
- URL expire mechanism.
- Click count(number of times a URL is used).
- Redis cache.
