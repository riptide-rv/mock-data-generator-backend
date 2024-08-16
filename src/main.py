from controllers.AuthController import router as auth_router
from controllers.UserController import router as user_router
from controllers.ProjectController import router as project_router

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import models.model as model
from repositories.config import engine


origins = {
    "http://localhost",
    "http://localhost:3000",
    "*"
}   

app = FastAPI()
app.add_middleware(
   CORSMiddleware,
    allow_origins = origins,
    allow_credentials =True,
    allow_methods = ["*"],
    allow_headers= ["*"],
)
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(project_router)
model.Base.metadata.create_all(bind=engine)





