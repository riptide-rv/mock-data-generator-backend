from fastapi import  FastAPI


from controllers.AuthController import router as auth_router
from controllers.UserController import router as user_router

app = FastAPI()
app.include_router(auth_router)
app.include_router(user_router)


