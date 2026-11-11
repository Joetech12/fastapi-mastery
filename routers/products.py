
from fastapi import APIRouter, Depends, HTTPException, status

from schemas.product import ProductCreate, ProductResponse
from services.product_service import ProductService


router = APIRouter()


@router.get("/", response_model=list[ProductResponse])
def get_products(
    product_service: ProductService = Depends(ProductService)
):

    return product_service.get_all_products()


@router.get("/{product_id}", response_model=ProductResponse)
def get_product(
    product_id: int,
    product_service: ProductService = Depends(ProductService)
):

    product = product_service.get_product_by_id(product_id)

    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )

    return product


@router.post(
    "/",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED
)
def create_product(
    product_data: ProductCreate,
    product_service: ProductService = Depends(ProductService)
):

    try:

        new_product = product_service.create_product(product_data)

        return new_product

    except ValueError as error:

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(error)
        )
