from pydantic import BaseModel

# Pydantic model used to defined and validate the structure of incoming JSON data 
class EventSchema(BaseModel):
    """ Event Schema """
    event_id: str
    event_type: str
    event_data: dict
