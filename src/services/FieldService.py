from repositories import FieldReposititory as field_repository
from models.Field import FieldCreate
from sqlalchemy.orm import Session
from uuid import UUID

def create_field(field: FieldCreate, db: Session):
    return field_repository.create_field(field, db)

def get_fields(project_id: UUID, db: Session):
    return field_repository.get_fields(project_id, db)