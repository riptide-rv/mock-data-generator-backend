from repositories import FieldReposititory as field_repository
from models.Field import FieldCreate, FieldUpdate
from sqlalchemy.orm import Session
from uuid import UUID
from services import ProjectService as project_service
from fastapi import HTTPException, status
from models.User import UserBase

def create_field(current_user: UserBase, project_id: UUID,field: FieldCreate, db: Session):
    project = project_service.get_project_by_id(current_user, project_id, db)
    if project is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="Project not found")
    return field_repository.create_field(project_id,field, db)

def get_fields(project_id: UUID, db: Session):
    return field_repository.get_fields(project_id, db)

def get_fields_by_project_id(project_id: UUID, db: Session):
    return field_repository.get_fields(project_id, db)

def update_field(project_id: UUID, field_id: UUID, field: FieldUpdate, db: Session):
    update_field = field_repository.update_field(project_id, field_id, field, db)
    if not update_field:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="Field not found")
    return update_field

def update_fields(project_id: UUID, fields: list[FieldUpdate], db: Session):
    updated_fields = field_repository.update_fields(project_id, fields, db)
    if not updated_fields:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="Field not found")
    return updated_fields

def delete_fields(project_id: UUID, fields: list[UUID], db: Session):
    deleted_fields = field_repository.delete_fields(project_id, fields, db)

    return deleted_fields


def delete_field(project_id: UUID, field_id: UUID, db: Session):
    deleted_field = field_repository.delete_field(project_id, field_id, db)
    if not deleted_field:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="Field not found")
    return deleted_field