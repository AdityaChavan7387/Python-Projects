# app/main.py
from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.database import Base, engine
from app.routes import item_routes, order_routes, bill_routes
from app.models import item_model, order_model, order_item_model
from app.routes import auth_routes, dept_routes

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mini Hotel Belling System")

@app.get("/")
def health():
    return {"status": "running"}

app.include_router(auth_routes.router)
app.include_router(dept_routes.router)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    Base.metadata.create_all(bind=engine)
    yield
    # Shutdown logic (optional)


app = FastAPI(
    title="Mini Hotel Billing System",
    lifespan=lifespan
)

app.include_router(item_routes.router, prefix="/api/items")
app.include_router(order_routes.router, prefix="/api/orders")
app.include_router(bill_routes.router, prefix="/api/bills")
