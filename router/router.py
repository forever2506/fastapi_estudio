from fastapi import APIRouter #divide las rutas

user = APIRouter()

@user.get("/")
def root():
    return {"message": "Hi, I am router FastAPI"}

