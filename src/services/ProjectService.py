from sqlalchemy.orm import Session
from uuid import UUID
from models.Project import GenerateType, ProjectCreate, ProjectUpdate
from models.User import UserBase
from repositories import ProjectRepository as project_repository
from fastapi import HTTPException, status

project_not_found_exception = HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="Project not found")


def create_project(project: ProjectCreate, current_user: UserBase, db: Session):
    return project_repository.create_project(project, current_user.id, db)

def get_projects(current_user: UserBase, db: Session):
    return project_repository.get_projects(current_user.id, db)

def get_project_by_id(current_user: UserBase, project_id: UUID, db: Session):
    project = project_repository.get_project_by_id(current_user.id, project_id, db)
    if project is None:
        raise project_not_found_exception
    return project

def update_project(project_id: UUID, project: ProjectUpdate, db: Session):
    updated_project = project_repository.update_project(project_id, project, db)
    if updated_project is None:
        raise project_not_found_exception
    return updated_project


def generate_mock_data(project_id: UUID, nor: int, format: GenerateType, current_user: UserBase, db: Session):
    project = project_repository.get_project_by_id(current_user, project_id, db)
    if project is None:
        raise project_not_found_exception
    res = generate_csv(project, nor)
    if format == GenerateType.JSON:
        res = convert_to_json(res)
    return res
    
def generate_csv(project, nor):
    res = []
    row = []
    for field in project.fields:
        row.append(field.name)
    res.append(row)
    return res

def convert_to_json(res):
    pass