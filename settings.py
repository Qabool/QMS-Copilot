import os
import streamlit as st
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
SOURCE_DOCS_DIR = DATA_DIR / "source_documents"
EVIDENCE_DIR = DATA_DIR / "evidence"
GENERATED_DOCS_DIR = DATA_DIR / "generated_documents"
VECTORSTORE_DIR = DATA_DIR / "vectorstore" / "iso_faiss_index"

for d in [SOURCE_DOCS_DIR, EVIDENCE_DIR, GENERATED_DOCS_DIR, VECTORSTORE_DIR.parent]:
    d.mkdir(parents=True, exist_ok=True)

def get_api_key(provider: str = "gemini") -> str:
    key_name = f"{provider.upper()}_API_KEY"
    try:
        if key_name in st.secrets:
            return st.secrets[key_name]
    except Exception:
        pass
    return os.getenv(key_name, "")
