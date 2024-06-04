from __future__ import annotations

import uuid
from typing import Type, Optional

from db import session
from db.base_class import Base
from pydantic import BaseModel
from starlette import status
from starlette.responses import JSONResponse

from sqlalchemy.orm import Session

from db.schemas.schemas import Product


class CRUDBase:
    def __init__(self, model: Type[Base]):
        self.model = model

    def create(self, db: Session, db_item: Type[BaseModel]):
        db_item = self.model(**db_item.dict())
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    def get_by_id(self, db: Session, id: uuid.UUID | str) -> Optional[Base]:
        return db.query(self.model).filter(self.model.id == id).first()

    def get_all(self, db: Session) -> list[Type[Base]]:
        import pydevd_pycharm
        pydevd_pycharm.settrace('localhost', port=7878, stdoutToServer=True, stderrToServer=True)
        return db.query(self.model).all()

    def update(self, db: Session, id: uuid.UUID | str, db_item: Type[BaseModel]):
        item = db.get(self.model, id)
        if not item:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={
                    "message": (
                        f"item with id {id} was not found"
                    )
                },
            )
        query = db.query(self.model).filter_by(id=id)
        db_item_ = query.first()
        query.update(db_item.dict())
        db.commit()
        db.refresh(db_item_)
        return db_item_

    def delete(self, db: Session, id: uuid.UUID | str):
        item = db.get(self.model, id)
        if not item:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={
                    "message": (
                        f"item with id {id} was not found"
                    )
                },
            )
        db_item = db.query(self.model).filter_by(id=id).first()
        db.delete(db_item)
        db.commit()
        response = JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "message": (
                    f"item with id {id} successfully deleted"
                )
            },
        )
        return response

