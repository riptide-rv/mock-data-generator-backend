from models.model import Project
from models.Project import ProjectCreate, ProjectBase, ProjectUpdate
from sqlalchemy.orm import Session
from uuid import UUID
from models.Field import FieldBase

def create_project(project: ProjectCreate, current_user: UUID, db: Session):
    new_project = Project(name=project.name, description=project.description, owner_id=current_user)
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    project = ProjectBase(**new_project.__dict__)
    return project

def get_projects(current_user: UUID, db: Session):
    projects =  db.query(Project).filter(Project.owner_id == current_user).all()
    projects = [ProjectBase(**project.__dict__) for project in projects]
    return projects

def get_project_by_id(current_user: UUID, project_id: UUID, db: Session):
    project =  db.query(Project).filter(Project.id == project_id and Project.owner_id == current_user).first()
    if project is None:
        return None
    project = ProjectBase(**project.__dict__, fields=[FieldBase(**field.__dict__) for field in project.fields])
    return project

def update_project(project_id: UUID, project: ProjectUpdate, db: Session):
    updated_project = db.query(Project).filter(Project.id == project_id).first()
    if updated_project is None:
        return None
    for key, value in project.__dict__.items():
        setattr(updated_project, key, value)
    db.commit()
    db.refresh(updated_project)
    updated_project = ProjectBase(**updated_project.__dict__)
    return updated_project