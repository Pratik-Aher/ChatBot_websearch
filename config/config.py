import os

# API Keys
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY", "")

# Groq default model
GROQ_DEFAULT_MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"

# RAG settings
CHUNK_SIZE = 1200
CHUNK_OVERLAP = 150
VECTOR_DIR = "vectorstore"
