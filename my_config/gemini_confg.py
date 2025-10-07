from decouple import config
from agents import AsyncOpenAI, OpenAIChatCompletionsModel,set_tracing_disabled

set_tracing_disabled(True)

key = config("GEMINI_API_KEY")
base_url = config("base_url")
Model = config("Gemini_model")

gemini_client = AsyncOpenAI(api_key=key,base_url=base_url)

MODEL = OpenAIChatCompletionsModel(model=Model, openai_client=gemini_client)
