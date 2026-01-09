from sqlalchemy.orm import Session
from app.models.item_model import ItemMaster

def create_item(db: Session, item):
    db_item = ItemMaster(name=item.name, rate=item.rate)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_all_items(db: Session):
    return db.query(ItemMaster).all()

def update_item_rate(db: Session, item_id: int, item):
    db_item = db.query(ItemMaster).filter(ItemMaster.id == item_id).first()
    if not db_item:
        return None

    db_item.rate = item.rate
    db.commit()
    db.refresh(db_item)
    return db_item

def update_item_name(db: Session, item_id: int, new_name: str):
    db_item = db.query(ItemMaster).filter(ItemMaster.id == item_id).first()
    if not db_item:
        return None

    db_item.name = new_name # type: ignore
    db.commit()
    db.refresh(db_item)
    return db_item
