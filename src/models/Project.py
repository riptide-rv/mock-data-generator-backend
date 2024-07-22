from models.Field import FieldDetails
from pydantic import BaseModel
from uuid import UUID
from typing import List

class ProjectBase(BaseModel):
    id: UUID 
    name: str
    description: str
    owner_id: UUID 
    fields: List[FieldDetails] | None = None 

class ProjectCreate(BaseModel):
    name: str
    description: str