import os
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from config.settings import VECTORSTORE_DIR
from typing import List, Dict, Any

class LocalFAISSRetriever:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        if VECTORSTORE_DIR.exists():
            self.vectorstore = FAISS.load_local(
                str(VECTORSTORE_DIR), 
                self.embeddings, 
                allow_dangerous_deserialization=True
            )
        else:
            self.vectorstore = None

    def similarity_search(self, query: str, k: int = 4) -> List[Dict[str, Any]]:
        if not self.vectorstore:
            return [{"text": "FAISS Index not found in data/vectorstore/iso_faiss_index. Please add your index.", "metadata": {}}]
        
        results = self.vectorstore.similarity_search_with_score(query, k=k)
        formatted = []
        for doc, score in results:
            formatted.append({
                "text": doc.page_content,
                "metadata": doc.metadata,
                "score": float(score)
            })
        return formatted