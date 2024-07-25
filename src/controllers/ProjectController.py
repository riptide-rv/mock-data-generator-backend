from fastapi import APIRouter, Depends
from dependencies import oauth2_scheme
from models.Project import ProjectBase, ProjectCreate, ProjectUpdate
from models.User import UserBase
from repositories.config import db_dependency
from models.model import Project
from services import UserService as user_service
from services import ProjectService as project_service
from typing import Annotated
from uuid import UUID
from services import FieldService as field_service
from models.Field import FieldCreate, FieldUpdate



router = APIRouter(prefix="/projects")
router.dependencies = [Depends(oauth2_scheme)]

@router.post("/")
async def create_project(
    project: ProjectCreate, current_user: Annotated[UserBase, Depends(user_service.get_current_active_user)], db: db_dependency
):
    new_project = project_service.create_project(project, current_user, db)
    return new_project

@router.get("/")
async def read_projects(current_user: Annotated[UserBase, Depends(user_service.get_current_active_user)], db: db_dependency):
    return project_service.get_projects(current_user, db)

@router.get("/{project_id}")
async def read_project(project_id: UUID, current_user: Annotated[UserBase, Depends(user_service.get_current_active_user)], db: db_dependency):
    return project_service.get_project_by_id(current_user, project_id, db)

@router.patch("/{project_id}")
async def update_project(
    project_id: UUID, project: ProjectUpdate, current_user: Annotated[UserBase, Depends(user_service.get_current_active_user)], db: db_dependency
):
    return project_service.update_project(project_id, project, db)

@router.post("/{project_id}/fields")
async def create_field(
    project_id: UUID, field: FieldCreate, current_user: Annotated[UserBase, Depends(user_service.get_current_active_user)], db: db_dependency
):
    return field_service.create_field(current_user, project_id, field, db)

@router.get("/{project_id}/fields")
async def get_fields_by_project_id(project_id: UUID, current_user: Annotated[UserBase, Depends(user_service.get_current_active_user)], db: db_dependency):
    return field_service.get_fields_by_project_id(project_id, db)

@router.put("/{project_id}/fields/{field_id}")
async def update_field(
    project_id: UUID, field_id: UUID, field: FieldUpdate, current_user: Annotated[UserBase, Depends(user_service.get_current_active_user)], db: db_dependency
):
    return field_service.update_field(project_id, field_id, field, db)

@router.put("/{project_id}/fields")
async def update_fields(
    project_id: UUID, fields: list[FieldUpdate], current_user: Annotated[UserBase, Depends(user_service.get_current_active_user)], db: db_dependency
):
    return field_service.update_fields(project_id, fields, db)