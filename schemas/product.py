
from pydantic import BaseModel, Field


class ProductCreate(BaseModel):
    sku: str = Field(
        pattern=r"^PROD-\d{4}$"
    )

    name: str = Field(
        min_length=3,
        max_length=100
    )

    category: str = Field(
        min_length=3,
        max_length=50
    )

    price: float = Field(
        gt=0
    )

    stock: int = Field(
        ge=0
    )
