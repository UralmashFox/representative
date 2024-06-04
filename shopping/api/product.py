from models.products import (ProductCreate as modelCreate,
                             ProductUpdate as modelUpdate,
                             ProductRead as modelRead)
from db.schemas.schemas import Product as Schema
from shopping.api.base import BasicRouter

product_router = BasicRouter(create_model=modelCreate, schema=Schema, update_model=modelUpdate, response_model=modelRead)
