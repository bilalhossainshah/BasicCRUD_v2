from fastapi import FastAPI
from database import get_conn
from routers import products,categorey,auth,cart
# from database import engine
# import models

app = FastAPI()
app.include_router(products.router)
app.include_router(categorey.router)
app.include_router(auth.router)
app.include_router(cart.router)

# models.Base.metadata.create_all(bind = engine)
# app.include_router(products.router)
# app.include_router(categorey.router)

