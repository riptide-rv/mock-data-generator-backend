from enum import Enum
from models.Field import FieldBase
from pydantic import BaseModel
from uuid import UUID

class GenerateType(Enum):
    JSON = "json"
    CSV = "csv"


class ProjectBase(BaseModel):
    id: UUID 
    name: str
    description: str
    owner_id: UUID 
    fields: list[FieldBase] = []

    def getFieldNames(self):
        field_names = []
        for field in self.fields:
            field_names.append(field.name)
        return field_names

    def jsonListString(self):
        json_string = ""
        for elem in self.fields:
            json_string += (elem.jsonString()+'\n')
            
        return json_string


class ProjectCreate(BaseModel):
    name: str
    description: str

class ProjectUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    description: str | None = None
    owner_id: UUID | None = None


