from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import tasks, users, budget, links, info
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(tasks.router)
app.include_router(budget.router)
app.include_router(links.router)
app.include_router(info.router)
from fastapi.responses import JSONResponse

@app.get("/")
def read_root():
    return JSONResponse(content={"message": "WeddingPlanner Backend is running!"})
