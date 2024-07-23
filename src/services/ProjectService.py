from sqlalchemy.orm import Session
from uuid import UUID
from models.Project import ProjectCreate
from models.User import UserBase
from repositories import ProjectRepository as project_repository
from fastapi import HTTPException, status

def create_project(project: ProjectCreate, current_user: UserBase, db: Session):
    return project_repository.create_project(project, current_user.id, db)

def get_projects(current_user: UserBase, db: Session):
    return project_repository.get_projects(current_user.id, db)

def get_project_by_id(current_user: UserBase, project_id: UUID, db: Session):
    project_not_found_exception = HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="Project not found")
    project = project_repository.get_project_by_id(current_user.id, project_id, db)
    if project is None:
        raise project_not_found_exception
    return project