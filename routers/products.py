
# from pydantic import BaseModel
# from sqlalchemy.orm import Session
# from fastapi import HTTPException,FastAPI
# import models,database


# class ProductBase(BaseModel):
#     name:str
#     price:float
#     description:str
#     cat_id:float

# router = APIRouter(prefix="/products",tags=["Products"])

# def get_db():
#     db = database.SessionLocal()
#     try:
#         yield db

#     finally:
#         db.close()

# @app.post("/products")
# def create_product():
    # categorey = db.query(models.Categorey).filter(models.Categorey.id == product.cat_id ).first()
    # if not categorey:
    #     raise HTTPException(status_code=400,detail="Categorey Not Found")
    
    # db_products = models.Products(
    #     name = product.name,
    #     price = product.price,
    #     description = product.description,
    #     cat_id = product.cat_id
    # )

    # db.add(db_products)
    # db.commit()
    # db.refresh(db_products)
    # return db_products
    # return {'message':"Items created successfully",'product':product}


    # products = db.query(models.Products).all()
    # result = [] 
    # for p in products:
    #     result.append({
    #         "id" : p.id,
    #         "price" : p.price,
    #         "description" : p.description,
    #         "ctegorey" : p.categorey.name if p.categorey else None
    # })
    # return result


# @app.put("/products:{/product_id}")
# def update_products():
    # db_products = db.query(models.Products).filter(models.Products.id == products_id).first()
    # if not db_products:
    #     raise HTTPException(status_code=404,detail="Product not found")
    
    # categorey = db.query(models.Categorey).filter(models.Categorey.id == product.cat_id).first()
    # if not categorey:
    #     raise HTTPException(status_code=404,detail="There is no Category ")
    
    # db_products.name = update_product.name
    # db_products.price = update_product.price
    # db_products.description = update_product.description
    # db_products.id = update_product.id
    
    # db.commit()
    # db.refresh(db_products)

    # return{"message":"Product updated Successfully",'product':db_products}


# @app.delete()
# def delete_product():
    # product = db.query(models.Products).filter(models.Products.id == product_id).first()
    # if not product:
    #     raise HTTPException(status_code=404,detail="Product not found")
    # db.delete(product)
    # db.commit()
     #return{"message":f"Successfully deleted {product_id}"}
from fastapi import APIRouter
from database import get_conn
# from models import create_tables

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/get")
def get_products():
    conn  = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT *from Prodts")
    products = cursor.fetchall()
    return [dict(row) for row in products]
@router.post("/create")
def create_product(name:str,description:str,price:float,cat_id:float):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("Insert into Products (name,description,price,cat_id )values(?,?,?,?)",(name,description,price,cat_id))
    conn.commit()
    conn.close()
    return {"message":"Produts Added Successfully"}

@router.put("/update")
def update_product(id:int,name:str,description:str,price:float,cat_id:float):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("Update Products set name =?, description = ?,price = ?,cat_id = ? where id=?",(name ,description,price,cat_id,id))

    conn.commit()
    conn.close()
    return{"message":"Products updated successfully"}