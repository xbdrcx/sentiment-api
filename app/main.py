from typing import List
from transformers import pipeline
from fastapi import FastAPI, APIRouter
from schemas import *
import torch
torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load model for sentiment analysis
sentiment_pipeline = pipeline("sentiment-analysis")

# Initialize FastAPI app
app = FastAPI(
    title="Sentiment Analysis API",
    description="A simple API for performing sentiment analysis on text using Hugging Face Transformers. Submit text and receive a sentiment label and confidence score."    
)

# Define router
router = APIRouter()
router.include_router(router, prefix="/sentiment", tags=["sentiment"])

@router.get("/", tags=["utility"])
def root():
    return { "message": "Welcome to Sentiment Analysis API 1.0" }

@router.post("/analyze", response_model=List[SentimentOutput])
def analyze(inputs: List[TextInput]):
    results = []
    for input in inputs:
        result = sentiment_pipeline(input.text)[0]
        results.append(SentimentOutput(label=result["label"], score=result["score"]))
    return results

app.include_router(router)
