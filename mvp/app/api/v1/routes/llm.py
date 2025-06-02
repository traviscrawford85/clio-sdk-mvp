# place holder for LLM-related routes
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict
router = APIRouter()

# Initialize the LLM service (for MVP, use OpenAI API directly)
class LLMRequestModel(BaseModel):
    prompt: str
    model: str = "gpt-3.5-turbo"
    max_tokens: int = 1000

class LLMResponseModel(BaseModel):
    response: str
    usage: Dict[str, int]

import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")

@router.post("/llm/generate", response_model=LLMResponseModel)
async def generate_llm_response(request: LLMRequestModel):
    try:
        completion = openai.ChatCompletion.create(
            model=request.model,
            messages=[{"role": "user", "content": request.prompt}],
            max_tokens=request.max_tokens,
        )
        response_text = completion.choices[0].message["content"]
        usage = completion.usage if hasattr(completion, "usage") else {}
        return LLMResponseModel(response=response_text, usage=usage)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))