from models.model import FieldDetail, Project
from models.Field import FieldCreate, FieldBase
from sqlalchemy.orm import Session
from uuid import UUID


def create_field(field: FieldCreate, db: Session):
    new_field = FieldDetail(**field.__dict__)
    db.add(new_field)
    db.commit()
    db.refresh(new_field)
    field = FieldBase(**new_field.__dict__)
    return field

def get_fields(project_id: UUID, db: Session):
    project =  db.query(Project).filter(id == project_id).first()
    fields = [FieldBase(**field.__dict__) for field in project.fields]
    return fields