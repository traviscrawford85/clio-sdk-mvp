# clio_ai/providers/openai_agent_service.py
import os
import openai
from clio_sdk.interfaces.i_llm_agent_service import ILLMAgentService

class OpenAIAgentService(ILLMAgentService):
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    async def run(self, prompt: str, context: dict = {}) -> str:
        response = await openai.ChatCompletion.acreate(
            model="gpt-4",
            messages=[
                {"role": "system", "content": context.get("system_prompt", "You are a legal assistant.")},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
