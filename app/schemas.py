from pydantic import BaseModel

# Pydantic model used to defined and validate structure of user input 
class TextInput(BaseModel):
    """ User Input Schema """
    text: str

# Pydantic model used to defined and validate structure of the sentiment analysis
class SentimentOutput(BaseModel):
    """ Sentiment Output Schema """
    label: str
    score: float
