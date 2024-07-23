from fastapi import APIRouter, Depends
from dependencies import oauth2_scheme
from models.Project import ProjectBase, ProjectCreate
from models.User import UserBase
from repositories.config import db_dependency
from models.model import Project
from services import UserService as user_service
from services import ProjectService as project_service
from typing import Annotated
from uuid import UUID



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
