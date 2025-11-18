from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src import extensions
from src.config import Settings
from src.routes import task_router
from src.database import connect_database, close_database


@asynccontextmanager
async def lifespan(app: FastAPI):
    extensions.settings = Settings()
    connect_database()
    yield
    extensions.settings = None
    close_database()



app = FastAPI(lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          
    allow_credentials=True,
    allow_methods=["*"],            
    allow_headers=["*"],         
)


app.include_router(task_router, prefix="/api/tasks", tags=["task"])