from fastapi import APIRouter
from database import get_conn

router = APIRouter(prefix="/cart" , tags=["Cart"])

@router.get("/Orders")
def get_orders(user_id:int):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(
        """
        Select cart.id,Users.username,Products.description,Products.price,cart.oreder_time
        from cart
        JOIN Users ON cart.user_id = Users.id
        JOIN Products ON cart.product_id = Products.id
        where cart.user_id = ?
        """,(user_id,)
    )
    orders = cursor.fetchall()

    cursor.execute("""
    select SUM(Products.price) as total_price
    from cart
    join products on cart.product_id = Products.id
    where cart.user_id = ?
""",(user_id,))
    total = cursor.fetchone()
    conn.close()
    return {
        "orders": [dict(row) for row in orders],
        "total_price": total["total_price"] if total["total_price"] else 0
        }

@router.post("/order")
def create_order( user_id:int, product_id:int):
    conn = get_conn()
    cursor = conn.cursor()
  
    cursor.execute("insert into Cart (user_id,product_id) values(?,?)",(user_id,product_id))
    conn.commit()
    conn.close()
    return{"message":"Order Added successfully"}

@router.get("/Grand_Total")
def get_total(use):
    conn = get_conn()
    cursor = conn.cursor()

    
    