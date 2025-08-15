"""Main application file for the FastAPI server."""

from fastapi import FastAPI, HTTPException

from models.tweet_url import TweetURL
from models.tweet_response import TweetResponse

from analyzers.fact_checker import fact_check_claim

from search.google_search import google_search

app = FastAPI()

@app.post("/analyze-tweet", response_model=TweetResponse)
async def analyze_tweet(data: TweetURL):
    """Endpoint to analyze a tweet given its URL."""
    try:
        response = await fact_check_claim(data.url)
        
        return response
    except ValueError as exc:
        raise HTTPException(status_code=400, detail="Invalid tweet URL format") from exc
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e



@app.get("/debug/google-search")
async def debug_google_search(q: str, n: int = 5):
    try:
        return await google_search(q, num_results=n)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e