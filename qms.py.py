from pydantic import BaseModel, Field
from typing import List, Optional

class QMSDocument(BaseModel):
    document_id: str
    title: str
    doc_type: str
    revision: str
    owner: str
    department: str
    status: str = "DRAFT"
    file_path: str
    referenced_clauses: List[str] = Field(default_factory=list)

class QMSGap(BaseModel):
    gap_id: str
    iso_clause: str
    document_id: Optional[str] = None
    status: str = "YELLOW"
    description: str
    risk_level: str
    recommended_action: str
    evidence_required: List[str] = Field(default_factory=list)