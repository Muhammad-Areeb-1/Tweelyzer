"""Main application file for the FastAPI server."""

from fastapi import FastAPI, HTTPException

from extractors.tweet_extractor import extract_tweet_data
from models.tweet_url import TweetURL
from models.tweet_response import TweetResponse
from analyzers.sentiment_analyzer import analyze_sentiment
from analyzers.claim_detector import detect_claim

app = FastAPI()

@app.post("/analyze-tweet", response_model=TweetResponse)
async def analyze_tweet(data: TweetURL):
    """Endpoint to analyze a tweet given its URL."""
    try:
        tweet = await extract_tweet_data(data.url)

        tweet['sentiment'] = analyze_sentiment(tweet['text'])
        tweet['is_claim'] = detect_claim(tweet['text'])
        
        return tweet
    except ValueError as exc:
        raise HTTPException(status_code=400, detail="Invalid tweet URL format") from exc
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
