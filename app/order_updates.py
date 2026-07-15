from database import get_connection

def update_order_status(order_id, status):

    connection = get_connection()

    cursor = connection.cursor()

    query = """
    UPDATE orders
    SET status = %s
    WHERE client_order_id = %s
    """

    cursor.execute(
        query,
        (
            status,
            order_id
        )
    )

    connection.commit()

    cursor.close()
    connection.close()

if __name__ == "__main__":

    update_order_status(
        "ORD001",
        "FILLED"
    )

    print("Order status updated")

