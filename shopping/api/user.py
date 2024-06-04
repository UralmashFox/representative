from models.users import (UserCreate as modelCreate,
                          UserUpdate as modelUpdate,
                          UserRead as modelRead)
from db.schemas.schemas import User as Schema
from shopping.api.base import BasicRouter
from crud.user import UserCRUD as CRUDService

user_router = BasicRouter(create_model=modelCreate, schema=Schema, update_model=modelUpdate,
                          response_model=modelRead, CRUDService=CRUDService)
