from pydantic import BaseModel


class Product(BaseModel):
    name: str
    cost: int

    class Config:
        from_attributes = True


class ProductCreate(Product):
    pass


class ProductRead(Product):
    id: int


class ProductUpdate(Product):
    pass

