from controllers.AuthController import router as auth_router
from controllers.UserController import router as user_router
from controllers.ProjectController import router as project_router

from fastapi import FastAPI
import models.model as model
from repositories.config import engine




app = FastAPI()
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(project_router)
model.Base.metadata.create_all(bind=engine)





