from typing import Type

from pydantic import BaseModel
from sqlalchemy.orm import Session

from crud.base import CRUDBase
from db.schemas.schemas import Product


class UserCRUD(CRUDBase):
    def create(self, db: Session, db_item: Type[BaseModel]):
        # import pydevd_pycharm
        # pydevd_pycharm.settrace('localhost', port=7878, stdoutToServer=True, stderrToServer=True)
        db_item_upd = {**db_item.dict()}
        products = db_item_upd['product_id']
        del db_item_upd['product_id']
        db_item = self.model(**db_item_upd)
        products_schemas = []
        for product in products:
            products_schemas.append(db.query(Product).where(Product.id == product).first())
        db_item.products = products_schemas
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
