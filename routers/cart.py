from fastapi import APIRouter
from database import get_conn

router = APIRouter(prefix="/cart", tags=["Cart"])

@router.get("/Orders")
def get_orders(user_id: int):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT Cart.id, Users.username, Products.description, Products.price, Cart.oreder_time
        FROM Cart
        JOIN Users ON Cart.user_id = Users.id
        JOIN Products ON Cart.product_id = Products.id
        WHERE Cart.user_id = ?
        """,
        (user_id,)
    )
    orders = cursor.fetchall()
    conn.close()

    return {
        "orders": [dict(row) for row in orders]
    }

@router.post("/order")
def create_order(user_id: int, product_id: int):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(" Select stock from Products where id = ?" ,(product_id,) )
    stock = cursor.fetchone()
    if not stock or stock[0]<=0:
        conn.close()
        return{"Message": "Product outof Stock!"}
    

    cursor.execute(
        "INSERT INTO Cart (user_id, product_id) VALUES (?, ?)",
        (user_id, product_id)
    )
    cursor.execute("""
    Update Products
    Set stock = stock-1
    Where id =? and stock > 0
    """,(product_id,))
    conn.commit()
    conn.close()
    return {"message": "Order added successfully"}

@router.post("/Checkout")
def checkout(user_id: int):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT Cart.id, Products.name, Products.price, Cart.oreder_time
        FROM Cart
        JOIN Products ON Cart.product_id = Products.id
        WHERE Cart.user_id = ?
    """, (user_id,))
    items = cursor.fetchall()

    if not items:
        conn.close()
        return {"message": "No items in cart for this user."}

    total_price = sum(item["price"] for item in items)

    cursor.execute("""
        INSERT INTO Orders (user_id, total_price)
        VALUES (?, ?)
    """, (user_id, total_price))

    cursor.execute("DELETE FROM Cart WHERE user_id = ?", (user_id,))

    conn.commit()
    conn.close()

    return {
        "message": "Checkout successful!",
        "total_price": total_price,
        "items": [dict(item) for item in items]
    }
