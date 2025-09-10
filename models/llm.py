from langchain_groq import ChatGroq
from config.config import GROQ_API_KEY, GROQ_DEFAULT_MODEL

def get_chatgroq_model():
    if not GROQ_API_KEY:
        raise ValueError("Missing GROQ_API_KEY.")
    try:
        return ChatGroq(
            api_key=GROQ_API_KEY,
            model=GROQ_DEFAULT_MODEL,
            temperature=0.7,
            max_tokens=500,
        )
    except Exception as e:
        raise RuntimeError(f"Failed to initialize Groq model: {e}")
