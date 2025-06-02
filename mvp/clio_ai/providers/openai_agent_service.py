# clio_ai/providers/openai_agent_service.py

import os
import openai
from clio_sdk.interfaces.i_llm_agent_service import ILLMAgentService

class OpenAIAgentService(ILLMAgentService):
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    async def run(self, prompt: str, context: dict = {}) -> str:
        system_msg = context.get("system_prompt", "You are a helpful assistant for legal tasks.")
        messages = [
            {"role": "system", "content": system_msg},
            {"role": "user", "content": prompt}
        ]
        response = await openai.ChatCompletion.acreate(
            model="gpt-4",
            messages=messages
        )
        return response.choices[0].message.content.strip()
