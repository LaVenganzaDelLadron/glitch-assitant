from pydantic import BaseModel, Field
from datetime import datetime

class Repository(BaseModel):
    id: str = Field(...)
    github_url: str = Field(...)
    owner: str = Field(...)
    name: str = Field(...)
    branch: str | None
    is_private: bool = Field(...)
    created_at: datetime = Field(...)