from pydantic import BaseModel, Field
from typing import List, Dict, Any

class PromptRequest(BaseModel):
    message: str = Field(..., description="Korisnička poruka")

class PromptResponse(BaseModel):
    intent: str
    confidence: float
    reply: str
    probs: Dict[str, float]
    trace: Dict[str, Any]

class IntentInfo(BaseModel):
    intent: str
    canonical_reply: str
    examples: List[str]

class IntentsResponse(BaseModel):
    intents: List[IntentInfo]