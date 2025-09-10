import numpy as np
from sentence_transformers import SentenceTransformer
from utils import doc_loader, vectorstore

# Use local embeddings for simplicity
_embedder = SentenceTransformer("all-MiniLM-L6-v2")
_vector_store = None

def ingest_files(uploaded_files):
    global _vector_store
    texts, metas = [], []
    for file in uploaded_files:
        text = doc_loader.load_text_from_file(file)
        chunks = doc_loader.recursive_character_splitter(text, chunk_size=1200, chunk_overlap=150)
        texts.extend(chunks)
        metas.extend([{"source": file.name}] * len(chunks))
    embeddings = np.array(_embedder.encode(texts))
    _vector_store = vectorstore.SimpleVectorStore(embeddings.shape[1])
    _vector_store.add(embeddings, texts, metas)

def retrieve(query, k=3):
    if not _vector_store:
        return []
    q_emb = np.array(_embedder.encode([query]))
    return _vector_store.search(q_emb, k=k)

def build_context_snippets(results):
    return "\n\n".join([f"[{i+1}] {r['text']}" for i, r in enumerate(results)])
