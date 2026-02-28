import chromadb
from chromadb.utils import embedding_functions

class MemorySystem:
    def __init__(self):
        self.client = chromadb.Client()

        self.embedding_function = embedding_functions.DefaultEmbeddingFunction()

        self.collection = self.client.get_or_create_collection(
            name="game_memory",
            embedding_function=self.embedding_function
        )

    def store(self, text):
        self.collection.add(
            documents=[text],
            ids=[str(hash(text))]
        )

    def retrieve(self, query, k=3):
        results = self.collection.query(
            query_texts=[query],
            n_results=k
        )
        return results["documents"][0] if results["documents"] else []