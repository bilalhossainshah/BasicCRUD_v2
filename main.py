<<<<<<< HEAD
from fastapi import FastAPI,Depends
from database import engine
import models
from routers import products,categorey,auth
=======
from fastapi import FastAPI
# from database import engine
# import models
from routers import products,categorey
>>>>>>> 505d644 (code just .db or product,catagories wli file mn h)

app = FastAPI()
app.include_router(products.router)
app.include_router(categorey.router)
<<<<<<< HEAD
app.include_router(auth.router)
=======
# models.Base.metadata.create_all(bind = engine)
# app.include_router(products.router)
# app.include_router(categorey.router)
>>>>>>> 505d644 (code just .db or product,catagories wli file mn h)

