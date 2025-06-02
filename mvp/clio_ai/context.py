# Context tracking for conversations
# clio_ai/context.py
from clio_ai.interfaces.i_llm_agent_service import ILLMAgentService
from clio_ai.providers.openai_agent_service import OpenAIAgentService

# Global binding for the current LLM agent service
llm_agent: ILLMAgentService = OpenAIAgentService()


agent_service: ILLMAgentService = OpenAIAgentService()
class Context:
    def __init__(self):
        self.conversation_history = []

    def add_message(self, role: str, content: str):
        self.conversation_history.append({"role": role, "content": content})

    def get_messages(self):
        return self.conversation_history

    async def run_agent(self, prompt: str) -> str:
        context = {"system_prompt": "You are a legal assistant."}
        return await agent_service.run(prompt, context)
    def clear(self):