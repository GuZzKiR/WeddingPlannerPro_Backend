from fastapi import APIRouter

router = APIRouter(prefix="/links", tags=["Links"])

@router.get("/")
def list_links():
    return {"message": "Ссылки"}