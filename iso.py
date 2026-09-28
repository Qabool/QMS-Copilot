from pydantic import BaseModel
from typing import Optional

class ISORequirement(BaseModel):
    document_id: str = "ISO9001-2026"
    document_title: str = "ISO 9001:2026 Quality management systems — Requirements"
    clause: str
    section: str
    requirement_summary: str
    source_chunk_id: str
    page_number: Optional[int] = None
    authority_level: int = 1
