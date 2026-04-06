import pydantic

class ProductCreate(pydantic.BaseModel):
    name: str
    description: str
    quantity: int
    price: float

class ProductResponse(ProductCreate):
    id: int

    class Config:
        orm_mode = True
