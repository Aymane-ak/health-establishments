from fastapi import APIRouter
from app.services.establishments_service import fetch_establishments 
router = APIRouter()

@router.get("/establishments")
def get_establishments():
    return fetch_establishments()
