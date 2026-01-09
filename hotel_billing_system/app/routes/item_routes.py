from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.item_schema import (
    ItemCreate,
    ItemUpdate,
    ItemNameUpdate,
    ItemResponse
)
from app.services import item_service
from app.utils.db_session import get_db

router = APIRouter(tags=["Items"])

@router.post("/", response_model=ItemResponse)
def create_item(
    item: ItemCreate,
    db: Session = Depends(get_db)
):
    return item_service.create_item(db, item)

@router.get("/", response_model=List[ItemResponse])
def get_items(
    db: Session = Depends(get_db)
):
    return item_service.get_all_items(db)

@router.put("/{item_id}", response_model=ItemResponse)
def update_item_rate(
    item_id: int,
    item: ItemUpdate,
    db: Session = Depends(get_db)
):
    updated_item = item_service.update_item_rate(db, item_id, item)

    if not updated_item:
        raise HTTPException(status_code=404, detail="Item not found")

    return updated_item

@router.put("/{item_id}/name", response_model=ItemResponse)
def update_item_name(
    item_id: int,
    payload: ItemNameUpdate,
    db: Session = Depends(get_db)
):
    return item_service.update_item_name(
        db=db,
        item_id=item_id,
        new_name=payload.name
    )