import abc
from google import genai
from config.settings import get_api_key

class BaseLLMProvider(abc.ABC):
    @abc.abstractmethod
    def generate(self, prompt: str, system_prompt: str = "") -> str:
        pass

class GeminiProvider(BaseLLMProvider):
    def __init__(self, model_name: str = "gemini-2.5-flash"):
        self.api_key = get_api_key("gemini")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY is not configured in Streamlit secrets or environment.")
        self.client = genai.Client(api_key=self.api_key)
        self.model_name = model_name

    def generate(self, prompt: str, system_prompt: str = "") -> str:
        full_prompt = f"System: {system_prompt}\n\nUser: {prompt}" if system_prompt else prompt
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=full_prompt
        )
        return response.text

def get_llm_provider(provider_name: str = "gemini", model_name: str = "gemini-2.5-flash") -> BaseLLMProvider:
    if provider_name.lower() == "gemini":
        return GeminiProvider(model_name=model_name)
    else:
        raise ValueError(f"Unsupported LLM provider: {provider_name}")