import os
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.language_models.chat_models import BaseChatModel


def get_llm() -> BaseChatModel:
    groq_key = os.getenv("GROQ_API_KEY")
    if groq_key:
        return ChatGroq(
            api_key=groq_key,
            model=os.getenv("GROQ_MODEL", "llama3-8b-8192"),
            temperature=0.1,
        )
    gemini_key = os.getenv("GEMINI_API_KEY")
    if gemini_key:
        return ChatGoogleGenerativeAI(
            google_api_key=gemini_key,
            model=os.getenv("GEMINI_MODEL", "gemini-1.5-flash"),
            temperature=0.1,
        )
    raise RuntimeError("No LLM API key configured. Set GROQ_API_KEY or GEMINI_API_KEY.")
