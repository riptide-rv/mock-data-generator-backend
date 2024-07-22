from enum import Enum
from pydantic import BaseModel
from uuid import UUID

class FieldType(Enum):
    STRING = "string"
    INTEGER = "integer"
    FLOAT = "float"
    BOOLEAN = "boolean"
    DATE = "date"

class FieldDetails(BaseModel):
    id: UUID
    name: str
    description: str
    type: FieldType
    project_id: UUID

