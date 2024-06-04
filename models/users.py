from pydantic import BaseModel
from typing import Optional

from models.products import ProductRead
from typing import List


class User(BaseModel):
    name: str

    class Config:
        from_attributes = True


class UserCreate(User):
    product_id: Optional[List[int]] = None
    pass


class UserRead(User):
    products: Optional[List[ProductRead]] = None
    id: int


class UserUpdate(User):
    pass

