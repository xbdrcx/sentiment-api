from pydantic import BaseModel, Field

# Pydantic model used to defined and validate structure of user input 
class TextInput(BaseModel):
    """ User Input Schema """
    text: str = Field(..., min_length=2, description="Text to analyze.")

# Pydantic model used to defined and validate structure of the sentiment analysis
class SentimentOutput(BaseModel):
    """ Sentiment Output Schema """
    label: str
    score: float
