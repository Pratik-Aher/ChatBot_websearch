import faiss
import numpy as np
import os
import pickle
from config.config import VECTOR_DIR

class SimpleVectorStore:
    def __init__(self, dim):
        self.index = faiss.IndexFlatL2(dim)
        self.texts = []
        self.metadatas = []

    def add(self, embeddings, texts, metadatas=None):
        self.index.add(embeddings.astype("float32"))
        self.texts.extend(texts)
        self.metadatas.extend(metadatas or [{}] * len(texts))

    def search(self, query_emb, k=3):
        D, I = self.index.search(query_emb.astype("float32"), k)
        return [{"text": self.texts[i], "metadata": self.metadatas[i]} for i in I[0]]

    def save(self, path=VECTOR_DIR):
        os.makedirs(path, exist_ok=True)
        faiss.write_index(self.index, os.path.join(path, "index.faiss"))
        with open(os.path.join(path, "texts.pkl"), "wb") as f:
            pickle.dump((self.texts, self.metadatas), f)

    @classmethod
    def load(cls, dim, path=VECTOR_DIR):
        index = faiss.read_index(os.path.join(path, "index.faiss"))
        with open(os.path.join(path, "texts.pkl"), "rb") as f:
            texts, metadatas = pickle.load(f)
        store = cls(dim)
        store.index = index
        store.texts = texts
        store.metadatas = metadatas
        return store
