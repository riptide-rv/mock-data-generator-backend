from enum import Enum
from pydantic import BaseModel
from uuid import UUID

class FieldType(Enum):
    STRING = "string"
    INTEGER = "integer"
    FLOAT = "float"
    BOOLEAN = "boolean"
    DATE = "date"

class FieldBase(BaseModel):
    id: UUID
    name: str
    description: str
    type: FieldType
    range: str
    project_id: UUID

class FieldCreate(BaseModel):
    name: str
    description: str
    type: FieldType
    range: str = ""
    project_id: UUID

