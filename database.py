# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
import sqlite3

def get_conn():
    db_path = "/home/bilal/get_post/BasicCRUD/pro.db"
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn
# DATABASE_URL = "sqlite:///./test.db"

# engine = create_engine(DATABASE_URL,connect_args={"check_same_thread":False})
# SessionLocal = sessionmaker(autoflush=False,autocommit=False,bind=engine)

# Base = declarative_base()

