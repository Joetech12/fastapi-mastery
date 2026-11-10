
from fastapi import APIRouter, Depends, HTTPException, status

from dependencies.pagination import pagination_params
from schemas.product import ProductCreate

router = APIRouter()


products = [
    {
        "id": 1,
        "sku": "PROD-1001",
        "name": "Laptop",
        "category": "electronics",
        "price": 1200000,
        "stock": 10
    },
    {
        "id": 2,
        "sku": "PROD-1002",
        "name": "Phone",
        "category": "electronics",
        "price": 750000,
        "stock": 15
    },
    {
        "id": 3,
        "sku": "PROD-1003",
        "name": "Chair",
        "category": "furniture",
        "price": 150000,
        "stock": 20
    },
    {
        "id": 4,
        "sku": "PROD-1004",
        "name": "Desk",
        "category": "furniture",
        "price": 250000,
        "stock": 8
    },
    {
        "id": 5,
        "sku": "PROD-1005",
        "name": "Headphones",
        "category": "electronics",
        "price": 85000,
        "stock": 30
    }
]


# GET: Retrieve all products with pagination
@router.get("/")
def get_products(
    pagination: dict = Depends(pagination_params)
):

    limit = pagination["limit"]
    offset = pagination["offset"]

    paginated_products = products[offset:offset + limit]

    return {
        "total": len(products),
        "limit": limit,
        "offset": offset,
        "products": paginated_products
    }


# GET: Filter products
@router.get("/search/filter")
def filter_products(
    category: str | None = None,
    max_price: float | None = None
):

    filtered_products = products

    if category is not None:
        filtered_products = [
            product for product in filtered_products
            if product["category"] == category
        ]

    if max_price is not None:
        filtered_products = [
            product for product in filtered_products
            if product["price"] <= max_price
        ]

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


# POST: Create a product
@router.post(
    "/",
    status_code=status.HTTP_201_CREATED
)
def create_product(product_data: ProductCreate):

    new_product = {
        "id": max(product["id"] for product in products) + 1,
        "sku": product_data.sku,
        "name": product_data.name,
        "category": product_data.category,
        "price": product_data.price,
        "stock": product_data.stock
    }

    products.append(new_product)

    return {
        "message": "Product created successfully",
        "product": new_product
    }
