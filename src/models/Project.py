from models.Field import FieldBase
from pydantic import BaseModel
from uuid import UUID


class ProjectBase(BaseModel):
    id: UUID 
    name: str
    description: str
    owner_id: UUID 
    fields: list[FieldBase] = []

class ProjectCreate(BaseModel):
    name: str
    description: str

class ProjectUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    description: str | None = None
    owner_id: UUID | None = None


