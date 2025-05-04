from fastapi import APIRouter

router = APIRouter(prefix="/budget", tags=["Budget"])

@router.get("/")
def list_budget():
    return {"message": "Бюджет"}