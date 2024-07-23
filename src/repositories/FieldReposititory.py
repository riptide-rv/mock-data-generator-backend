from models.model import FieldDetail, Project
from models.Field import FieldCreate, FieldBase, FieldUpdate
from sqlalchemy.orm import Session
from uuid import UUID


def create_field(project_id: UUID ,field: FieldCreate, db: Session):
    new_field = FieldDetail(**field.__dict__, project_id = project_id)
    db.add(new_field)
    db.commit()
    db.refresh(new_field)
    field = FieldBase(**new_field.__dict__)
    return field

def get_fields(project_id: UUID, db: Session):
    project =  db.query(Project).filter(Project.id == project_id).first()
    fields = [FieldBase(**field.__dict__) for field in project.fields]
    return fields

def get_field_by_id(project_id: UUID, field_id: UUID, db: Session):
    field =  db.query(FieldDetail).filter(FieldDetail.id == field_id and FieldDetail.project_id == project_id).first()
    if field is None:
        return None
    field = FieldBase(**field.__dict__)
    return field

def update_field(project_id: UUID, field_id: UUID, field: FieldUpdate, db: Session):
    field_ = get_field_by_id(project_id, field_id, db)
    update_field = FieldDetail(**field_.__dict__)
    if not field_:
        return None
    
    for key, value in field.__dict__.items():
        if value:
            setattr(update_field, key, value)
    db.merge(update_field)
    db.commit()
    return FieldBase(**update_field.__dict__)