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


def update_fields(project_id: UUID, fields: list[FieldUpdate], db: Session):
    updated_fields = []
    for field in fields:
        updated_field = update_field(project_id, field.id, field, db)
        if updated_field is None:
            return None
        updated_fields.append(updated_field)
    return updated_fields

def delete_fields(project_id: UUID, fields: list[UUID], db: Session):
    deleted_fields = []
    for field_id in fields:
        delete_field(project_id, field_id, db)
    return deleted_fields


def delete_field(project_id: UUID, field_id: UUID, db: Session):
    deleted_field = db.query(FieldDetail).filter(FieldDetail.id == field_id and FieldDetail.project_id == project_id).first()
    if deleted_field is None:
        return None
    db.delete(deleted_field)
    db.commit()
    return deleted_field