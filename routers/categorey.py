# from fastapi import APIRouter,Depends,HTTPException
# from sqlalchemy.orm import Session
# from pydantic import BaseModel
# import models
# from database import SessionLocal

# router = APIRouter(prefix="/categories", tags=["Categories"])

# class CatBase(BaseModel):
#     name :str

# def get_db():
#     db = SessionLocal()

#     try:
#         yield db

#     finally:
#         db.close()

# @router.post("/")
# def create_categorey(categorey: CatBase, db:Session = Depends(get_db)):
#     db_cat = models.Categorey(name = categorey.name)
#     db.add(db_cat)
#     db.commit()
#     db.refresh(db_cat)

#     return db_cat

# @router.get("/")
# def get_categories(db:Session = Depends(get_db)):
#     return db.query(models.Categorey).all()

# @router.put("/cat_id")
# def update_categorey(cat_id: int,categorey:CatBase, db:Session = Depends(get_db)):
#     db_cat = db.query(models.Categorey).filter(models.Categorey.id == cat_id).first()
#     if not db_cat:
#         raise HTTPException(status_code=400,detail="Catgorey Not found")
#     db_cat.name = categorey.name
#     db.commit()
#     return {"message":"Categorey updated Sucessfully"}

# @router.delete("/cat_id")
# def delete_categorey(cat_id: int , db:Session = Depends(get_db)):
#     db_cat = db.query(models.Categorey).filter(models.Categorey.id == cat_id).first()
#     if not db_cat:
#         raise HTTPException(status_code=401,detail="Catgorey Not Found")
#     db.delete(db_cat)
#     db.commit()

#     return{"message": "Categorey Deleted Successfully"}
from fastapi import APIRouter
from database import get_conn

router = APIRouter(prefix="/Catagory", tags=["Catagories"])

@router.get("/Get")
def get_category():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("Select *from Catagories")
    cat = cursor.fetchall()
    conn.commit()
    conn.close()
    return[dict(row) for row in cat]
@router.post("/Create")
def create_category(name:str):
    conn =get_conn()
    cursor = conn.cursor()
    cursor.execute("Insert into Catagories (name) values(?) ",(name,))
    conn.commit()
    conn.close()
    return{"message":"Category created successfully hahaha"}

