from pydantic import BaseModel, Field
from datetime import datetime

class Scan(BaseModel):
    id: str = Field(...)
    name: str = Field(...)
    repository_id: str = Field(...)
    status: str = Field(...) # queued, running, completed, failed
    started_at: datetime | None
    completed_at: datetime | None
    total_findings: int | None
    critical_count: int | None
    high_count: int | None
    error_message: str | None