from abc import ABC, abstractmethod
from google import genai
import os


# Base class for all LLM providers
class LLMProvider(ABC):

    @abstractmethod
    def generate(self, prompt):
        pass


# Gemini implementation
class GeminiProvider(LLMProvider):

    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)

    def generate(self, prompt):
        response = self.client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt,
            config={
                "http_options": {
                    "timeout": 30000
                }
            }
        )

        return response.text


# Main LLM Client
class LLMClient:

    def __init__(self, provider):
        self.provider = provider

    def generate(self, prompt):
        return self.provider.generate(prompt)