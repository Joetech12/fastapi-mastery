
from typing import Annotated, Literal

from pydantic import BaseModel, Field


ProductStatus = Literal[
    "active",
    "inactive",
    "discontinued"
]


class ProductCreate(BaseModel):

    sku: Annotated[
        str,
        Field(
            pattern=r"^PROD-\d{4}$",
            description="Unique product SKU"
        )
    ]

    name: Annotated[
        str,
        Field(
            min_length=3,
            max_length=100
        )
    ]

    category: Annotated[
        str,
        Field(
            min_length=3,
            max_length=50
        )
    ]

    price: Annotated[
        float,
        Field(gt=0)
    ]

    stock: Annotated[
        int,
        Field(ge=0)
    ] = 0

    status: ProductStatus = "active"


class ProductResponse(BaseModel):

    id: int
    sku: str
    name: str
    category: str
    price: float
    stock: int
    status: ProductStatus
