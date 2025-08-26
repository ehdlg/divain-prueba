from app.routes.product import router as product_router
from fastapi import FastAPI

app = FastAPI()

app.include_router(product_router, prefix="/products", tags=["/products"])


@app.get("/")
async def root():
    return {"message": "Welcome to the API"}
