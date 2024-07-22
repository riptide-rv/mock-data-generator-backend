from models.Field import FieldDetails
from pydantic import BaseModel
from uuid import UUID


class ProjectBase(BaseModel):
    id: UUID 
    name: str
    description: str
    owner_id: UUID 
    fields: list[FieldDetails] = []

class ProjectCreate(BaseModel):
    name: str
    description: str