from fastapi import APIRouter #divide las rutas
from schema.user_schema import UserSchema

user = APIRouter()

@user.get("/")
def root():
    return {"message": "Hi, I am router FastAPI"}

@user.post("api/user")
def create_user(data_user):
    print(data_user)

@user.put("/api/user")
def update_user():
    pass