import uuid
from typing import Type, Union, List

from fastapi import Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from crud.base import CRUDBase
from db.base_class import Base
from db.session import get_db
from fastapi import APIRouter


class CreateRouterMixin:
    @staticmethod
    def handle_create(schema: Type[Base], create_model: Type[BaseModel], response_model: Type[BaseModel],
                      CRUDService: Type[CRUDBase] = CRUDBase):
        async def _create(
                *,
                db: Session = Depends(get_db),
                db_item: create_model,
        ) -> response_model:
            db_item = CRUDService(schema).create(db=db, db_item=db_item)
            return response_model.from_orm(db_item)

        return _create


class GetRouterMixin:
    @staticmethod
    def handle_get(schema: Type[Base], response_model: Type[BaseModel], CRUDService: Type[CRUDBase] = CRUDBase):
        async def _get(
                *,
                db: Session = Depends(get_db)
        ) -> List[response_model]:
            db_item = CRUDService(schema).get_all(db=db)
            return [response_model.from_orm(item) for item in db_item]

        return _get


class PutRouterMixin:
    @staticmethod
    def handle_put(schema: Type[Base], update_model: Type[BaseModel], response_model: Type[BaseModel],
                   CRUDService: Type[CRUDBase] = CRUDBase):
        async def _put(
                *,
                db: Session = Depends(get_db),
                id: Union[uuid.UUID, str],
                db_item: update_model
        ) -> response_model:
            db_item = CRUDService(schema).update(db=db, id=id, db_item=db_item)
            return response_model.from_orm(db_item)

        return _put


class DeleteRouterMixin:
    @staticmethod
    def handle_delete(schema: Type[Base], CRUDService: Type[CRUDBase] = CRUDBase):
        async def _delete(
                *,
                db: Session = Depends(get_db),
                id: Union[uuid.UUID, str],
        ):
            response = CRUDService(schema).delete(db=db, id=id)
            return response

        return _delete


class GetByIDRouterMixin:

    @staticmethod
    def handle_get_by_id(schema: Type[Base],  response_model: Type[BaseModel], CRUDService: Type[CRUDBase] = CRUDBase):
        async def get_by_id(
                *,
                db: Session = Depends(get_db),
                id: Union[uuid.UUID, str]
        ) -> response_model:
            db_item = CRUDService(schema).get_by_id(db=db, id=id)
            return response_model.from_orm(db_item)

        return get_by_id


class CreateReadRouter(APIRouter, CreateRouterMixin, GetRouterMixin):

    def __init__(self, schema: Type[Base], create_model: Type[BaseModel], response_model: Type[BaseModel],
                 CRUDService: Type[CRUDBase] = CRUDBase):
        super().__init__()
        self.add_api_route("/", self.handle_create(schema=schema,
                                                   create_model=create_model,
                                                   response_model=response_model,
                                                   CRUDService=CRUDService),
                           methods=["POST"])
        self.add_api_route("/", self.handle_get(schema=schema,
                                                response_model=response_model,
                                                CRUDService=CRUDService),
                           methods=["GET"])


class BasicRouter(CreateReadRouter, GetByIDRouterMixin, PutRouterMixin, DeleteRouterMixin):
    def __init__(self, schema: Type[Base], create_model: Type[BaseModel], update_model: Type[BaseModel],
                 response_model: Type[BaseModel], CRUDService: Type[CRUDBase] = CRUDBase):
        super().__init__(schema=schema,
                         create_model=create_model,
                         CRUDService=CRUDService,
                         response_model=response_model)
        self.add_api_route("/{id}", self.handle_get_by_id(schema=schema,
                                                          response_model=response_model,
                                                          CRUDService=CRUDService),
                           methods=["GET"])
        self.add_api_route("/{id}",
                           self.handle_put(schema=schema,
                                           update_model=update_model,
                                           response_model=response_model,
                                           CRUDService=CRUDService),
                           methods=["PUT"])
        self.add_api_route("/{id}", self.handle_delete(schema=schema, CRUDService=CRUDService), methods=["DELETE"])
