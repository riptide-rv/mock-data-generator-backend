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

