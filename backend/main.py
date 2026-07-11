# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
import os

app = FastAPI(title="News Agent API")

DB_PATH = "news_agent.db"

# Pydantic model for POST /news/fetch
class FetchRequest(BaseModel):
    query: str
    limit: int = 10

# Initialize DB (creates file if missing)
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY,
            title TEXT,
            category TEXT,
            content TEXT,
            fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

@app.on_event("startup")
def on_startup():
    init_db()
    print("✅ Server starting on http://localhost:8000")

@app.get("/health")
def health():
    return {"status": "ok", "database": os.path.exists(DB_PATH)}

@app.get("/news/categories")
def get_categories():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM categories")
    categories = [row[0] for row in cursor.fetchall()]
    conn.close()
    return {"categories": categories}

@app.post("/news/fetch")
def fetch_news(request: FetchRequest):
    # Placeholder: replace with real fetching logic
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT OR IGNORE INTO categories (name) VALUES (?)", 
        (request.query,)
    )
    conn.commit()
    conn.close()
    return {"status": "fetched", "query": request.query, "limit": request.limit}

@app.get("/news/digest")
def get_digest():
    # Placeholder: return summarized news
    return {"digest": "No articles yet. Try POST /news/fetch first."}

# 👇 This is CRITICAL — without it, the server won't start when you run `python main.py`
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)