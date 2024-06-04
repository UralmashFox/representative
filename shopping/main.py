
from fastapi import FastAPI
from shopping.api.product import product_router
from shopping.api.user import user_router


app = FastAPI(title="Shop API", docs_url="/", version="1.0.0")

app.include_router(
    user_router,
    prefix="/user",
    tags=["Users"],
)

app.include_router(
    product_router,
    prefix="/product",
    tags=["Product"],
)



