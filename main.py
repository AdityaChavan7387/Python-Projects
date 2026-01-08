from fastapi import FastAPI
from app.routes import emp_routes

app = FastAPI(title="dummy routing demo")

@app.get("/")
def health_check():
    return {"status": "ok", "message": "app running"}

app.include_router(emp_routes.router)