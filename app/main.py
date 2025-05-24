from fastapi import FastAPI, APIRouter, HTTPException
from transformers import pipeline
from typing import List
from schemas import *
import torch, logging
torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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
    logger.info(f"Received {len(inputs)} texts for analysis")
    results = []
    for input in inputs:
        try :
            result = sentiment_pipeline(input.text)[0]
            logger.info(f"Text: {input.text} | Result: {result}")
            results.append(SentimentOutput(label=result["label"], score=result["score"]))
        except Exception as e:
            logger.error(f"Error analyzing text: {input.text} | Error: {str(e)}")
            raise HTTPException(status_code=500, detail=f"Error analyzing text: {str(e)}")
    return results

app.include_router(router)
