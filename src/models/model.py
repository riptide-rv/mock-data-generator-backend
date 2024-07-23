from sqlalchemy import Boolean, Column, String, Uuid, ForeignKey, Enum
from sqlalchemy.orm import relationship
from repositories.config import Base
from models.Field import FieldType
import uuid



class User(Base):
    __tablename__  = "users"
    id = Column(Uuid, primary_key=True, index=True, default=uuid.uuid4)
    username = Column(String(50), unique=True, index=True)
    hashed_password = Column(String(200))
    disabled = Column(Boolean, default = False)
    projects = relationship("Project", back_populates="owner")

class Project(Base):
    __tablename__ = "projects"
    id = Column(Uuid, primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String(50))
    description = Column(String(200))
    owner_id = Column(Uuid, ForeignKey('users.id'))
    owner = relationship("User", back_populates="projects")
    fields = relationship("FieldDetail", back_populates="project")

class FieldDetail(Base):
    __tablename__ = "fields"
    id = Column(Uuid, primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String(50))
    description = Column(String(200))
    type = Column(Enum(FieldType))
    range = Column(String(50))
    project_id = Column(Uuid, ForeignKey('projects.id'))
    project = relationship("Project", back_populates="fields")
    

    