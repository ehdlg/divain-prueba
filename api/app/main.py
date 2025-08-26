from app.routes.product import router as product_router
from app.routes.stock import router as stock_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5174"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(product_router, prefix="/products", tags=["/products"])
app.include_router(stock_router, prefix="/stock", tags=["/stock"])


@app.get("/")
async def root():
    return {"message": "Welcome to the API"}
