from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi import FastAPI, APIRouter, HTTPException, Request
from transformers import pipeline
from typing import List
from schemas import *
import torch, logging
torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load model for sentiment analysis
sentiment_pipeline = pipeline("text-classification", model="tabularisai/multilingual-sentiment-analysis")

# Define slowapi Rate Limiter
limiter = Limiter(key_func=get_remote_address)

# Initialize FastAPI app
app = FastAPI(
    title="Sentiment Analysis API",
    description="A simple API for performing sentiment analysis on text using Hugging Face Transformers. Submit text and receive a sentiment label and confidence score."    
)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Define router
router = APIRouter()
router.include_router(router, prefix="/sentiment", tags=["sentiment"])

@router.get("/", tags=["utility"])
def root():
    return { "message": "Welcome to Sentiment Analysis API 1.0" }

@router.post(
    "/analyze",
    summary="Analyze Sentiment",
    description="Analyze the sentiment of a list of texts and return the sentiment label and confidence score for each.",
    response_model=List[SentimentOutput],
    responses={
        200: {"description": "Successful sentiment analysis."},
        422: {"description": "Validation Error"},
        500: {"description": "Internal Server Error"}
    }
)
@limiter.limit("5/minute")  # Limit to 5 requests / minute per IP
def analyze(request: Request, inputs: List[TextInput]):
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
