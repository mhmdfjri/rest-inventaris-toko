from fastapi import FastAPI
from app.controllers import category, product
from app.database import engine
import app.models as models

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(category.api)
app.include_router(product.api)