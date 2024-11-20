from fastapi import FastAPI

from .database import Base, engine
from .routers import tariffs, calculator

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(tariffs.router, prefix="/api")
app.include_router(calculator.router, prefix="/api")
