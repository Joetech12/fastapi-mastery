
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_products():
    return {
        "products": [
            {"id": 1, "name": "Laptop", "price": 1200000},
            {"id": 2, "name": "Phone", "price": 750000}
        ]
    }


@router.get("/{product_id}")
def get_product(product_id: int):
    return {
        "id": product_id,
        "name": "Laptop",
        "price": 1200000
    }
