from fastapi import FastAPI
from app.database import Base, engine
from app.routes import dept_routes

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Department CRUD API")

@app.get("/")
def health_check():
    return {"status": "ok"}

app.include_router(dept_routes.router)