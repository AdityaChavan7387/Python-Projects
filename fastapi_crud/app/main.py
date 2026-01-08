from fastapi import FastAPI
from app.database import Base, engine
from app.routes import emp_routes, attend_routes
 
# Create tables at application startup
Base.metadata.create_all(bind=engine)
 
app = FastAPI(title="Rocket Co.")
 
@app.get("/")
def health_check():
 return {
           "status": "ok",
           "message": "API is running"
     } 

# Register routes
app.include_router(emp_routes.router)
app.include_router(attend_routes.router)