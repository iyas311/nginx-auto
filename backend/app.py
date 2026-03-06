from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Pydantic model for receiving product data
class Product(BaseModel):
    name: str
    category: str
    price: float

# A simple dictionary acting as an in-memory database
products = {
    1: {"name": "Laptop", "category": "Electronics", "price": 999.99},
    2: {"name": "Smartphone", "category": "Electronics", "price": 499.99},
    3: {"name": "Running Shoes", "category": "Sports", "price": 89.99},
    4: {"name": "Coffee Maker", "category": "Home", "price": 49.99}
}

@app.get("/api")
def hello():
    return {"message": "Hello from FastAPI"}

@app.get("/api/products")
def get_products():
    """Returns the list of all products."""
    return products

@app.get("/api/products/{product_id}")
def get_product(product_id: int):
    """Returns a specific product by its ID."""
    if product_id in products:
        return products[product_id]
    raise HTTPException(status_code=404, detail="Product not found")

@app.post("/api/products")
def add_product(product: Product):
    """Adds a new product to the dictionary."""
    # Generate a new ID (highest existing ID + 1)
    new_id = max(products.keys(), default=0) + 1
    
    # Add to the dictionary
    products[new_id] = product.dict()
    
    return {"message": "Product added successfully", "id": new_id, "product": products[new_id]}
