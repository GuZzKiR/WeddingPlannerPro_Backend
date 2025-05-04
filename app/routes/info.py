from fastapi import APIRouter

router = APIRouter(tags=["Info"])

@router.get("/about")
def get_about():
    return {
        "author": "Кирилл Гусев",
        "project": "WeddingPlanner Pro",
        "description": "Backend API для Telegram мини-приложения"
    }