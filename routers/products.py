
from fastapi import APIRouter, HTTPException

router = APIRouter()


products = [
    {"id": 1, "name": "Laptop", "category": "electronics", "price": 1200000},
    {"id": 2, "name": "Phone", "category": "electronics", "price": 750000},
    {"id": 3, "name": "Chair", "category": "furniture", "price": 150000},
    {"id": 4, "name": "Desk", "category": "furniture", "price": 250000},
    {"id": 5, "name": "Headphones", "category": "electronics", "price": 85000}
]


# GET: Retrieve all products
@router.get("/")
def get_products():
    return {
        "products": products
    }


# GET: Filter products by category
@router.get("/search/filter")
def filter_products(category: str):

    filtered_products = []

    for product in products:
        if product["category"] == category:
            filtered_products.append(product)

    return {
        "products": filtered_products
    }


# GET: Retrieve one product
@router.get("/{product_id}")
def get_product(product_id: int):

    for product in products:
        if product["id"] == product_id:
            return product

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )
