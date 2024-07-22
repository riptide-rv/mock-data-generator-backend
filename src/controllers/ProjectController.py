from fastapi import APIRouter, Depends
from dependencies import oauth2_scheme
from models.Project import ProjectBase, ProjectCreate
from models.User import UserBase
from repositories.config import db_dependency
from models.model import Project
from services import UserService as user_service
from typing import Annotated


router = APIRouter(prefix="/projects")
router.dependencies = [Depends(oauth2_scheme)]

@router.post("/")
async def create_project(
    project: ProjectCreate, current_user: Annotated[UserBase, Depends(user_service.get_current_active_user)], db: db_dependency
):
    new_project = Project(name=project.name, description=project.description, owner_id=current_user.id)
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project

@router.get("/")
async def read_projects(current_user: Annotated[UserBase, Depends(user_service.get_current_active_user)], db: db_dependency):
    return db.query(Project).filter(Project.owner_id == current_user.id).all()
