from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, database
from app.repository import category as category_repo

api = APIRouter(
    prefix="/categories",
    tags=["categories"],
)

@api.post("/", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(database.get_db)):
    return category_repo.create_category(db=db, category=category)

@api.get("/", response_model=List[schemas.Category])
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    categories = category_repo.get_categories(db, skip=skip, limit=limit)
    return categories

@api.put("/{category_id}", response_model=schemas.Category)
def update_category(category_id: int, category: schemas.CategoryCreate, db: Session = Depends(database.get_db)):
    return category_repo.update_category(db=db, category_id=category_id, category=category)

@api.delete("/{category_id}", response_model=schemas.Category)
def delete_category(category_id: int, db: Session = Depends(database.get_db)):
    return category_repo.delete_category(db=db, category_id=category_id)
