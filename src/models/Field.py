from enum import Enum
from pydantic import BaseModel
from typing import Optional
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

    def jsonString(self):
        format_string = (
            """{{{{
    'name': {name},
    'description':{description},
    'type':{type},
    'range':{range}
}}}},\n"""
        )
        return format_string.format(
            name=self.name,                                 
            description = self.description,
            range = self.range,
            type = self.type)

class FieldCreate(BaseModel):
    name: str
    description: str
    type: FieldType
    range: str = ""
   
class FieldUpdate(BaseModel):
    id: Optional[UUID] | None = None
    name: Optional[str]  | None = None
    description: Optional[str] | None = None
    type: Optional[FieldType] | None = None
    range: Optional[str] | None = None
    project_id: Optional[UUID] | None = None
