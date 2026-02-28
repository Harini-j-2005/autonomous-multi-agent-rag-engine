import chromadb
from chromadb.utils import embedding_functions

class MemorySystem:
    def __init__(self):
        self.client = chromadb.Client()
        self.collection = self.client.create_collection(
            name="game_memory",
            embedding_function=embedding_functions.DefaultEmbeddingFunction()
        )

    def store(self, text):
        self.collection.add(
            documents=[text],
            ids=[str(len(self.collection.get()["ids"]) + 1)]
        )

    def retrieve(self, query):
        results = self.collection.query(query_texts=[query], n_results=2)
        return results["documents"][0] if results["documents"] else []