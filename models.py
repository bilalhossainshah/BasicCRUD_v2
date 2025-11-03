<<<<<<< HEAD
from sqlalchemy import String,Column,Integer,ForeignKey
from database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)


class Products(Base):
    __tablename__ = "Products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Integer)
    description = Column(String)
    cat_id = Column(Integer, ForeignKey("Categorey.id"))
=======
# from sqlalchemy import String,Column,Integer,ForeignKey
# from database import get_conn
# from sqlalchemy.orm import relationship
# class Products(Base):
#     __tablename__ = "Products"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     price = Column(Integer)
#     description = Column(String)
#     cat_id = Column(Integer, ForeignKey("Categorey.id"))
>>>>>>> 505d644 (code just .db or product,catagories wli file mn h)
    
#     categories = relationship("Categorey",back_populates="product")


# class Categorey(Base):
#     __tablename__ = "Categorey"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, unique=True)


# #     product = relationship("Products", back_populates="categories")

# def create_tables():
#     conn = get_conn()
#     cursor = conn.cursor()
#     cursor.execute('''
#             create table product(
#                    id INTEGER PRIMARY KEY AUTOINCREMENT,
#                    name TEXT NOT NULL,
#                    description TEXT NOT NULL,
#                    price INTEGER NOT NULL
#                    )
# ''')
    
#     conn.commit()
#     conn.close()    