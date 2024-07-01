from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    description: str
    price: int
    category_id: int

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        from_attributes = True

class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int
    products: list[Product] = []

    class Config:
        from_attributes = True
