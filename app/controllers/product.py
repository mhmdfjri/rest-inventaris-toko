from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, database
from app.api import product as product_repo

api = APIRouter(
    prefix="/products",
    tags=["products"],
)

@api.post("/add", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(database.get_db)):
    return product_repo.create_product(db=db, product=product)

@api.get("/get-all", response_model=List[schemas.Product])
def read_products(db: Session = Depends(database.get_db)):
    return product_repo.get_products(db)

@api.get("/get/{id}", response_model=schemas.Product)
def read_product(product_id: int, db: Session = Depends(database.get_db)):
    db_product = product_repo.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@api.put("/update/{id}", response_model=schemas.Product)
def update_product(product_id: int, product: schemas.ProductCreate, db: Session = Depends(database.get_db)):
    return product_repo.update_product(db=db, product_id=product_id, product=product)

@api.delete("/delete/{id}", response_model=schemas.Product)
def delete_product(product_id: int, db: Session = Depends(database.get_db)):
    return product_repo.delete_product(db=db, product_id=product_id)
