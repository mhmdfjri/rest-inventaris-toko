from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, database
from app.api import category as category_repo

api = APIRouter(
    prefix="/categories",
    tags=["categories"],
)

@api.post("/add", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(database.get_db)):
    return category_repo.create_category(db=db, category=category)

@api.get("/get-all", response_model=List[schemas.Category])
def read_categories(db: Session = Depends(database.get_db)):
    categories = category_repo.get_categories(db)
    return categories

@api.get("/get/{id}", response_model=schemas.Category)
def read_category(category_id: int, db: Session = Depends(database.get_db)):
    db_category = category_repo.get_category(db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_category

@api.put("/update/{id}", response_model=schemas.Category)
def update_category(category_id: int, category: schemas.CategoryCreate, db: Session = Depends(database.get_db)):
    return category_repo.update_category(db=db, category_id=category_id, category=category)

@api.delete("/delete/{id}", response_model=schemas.Category)
def delete_category(category_id: int, db: Session = Depends(database.get_db)):
    return category_repo.delete_category(db=db, category_id=category_id)
