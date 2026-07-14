from database import get_connection


def save_order(order):

    connection = get_connection()

    cursor = connection.cursor()

    query = """
    INSERT INTO orders
    (client_order_id, symbol, side, quantity, price, status)
    VALUES (%s,%s,%s,%s,%s,%s)
    """

    cursor.execute(
        query,
        (
            order["client_order_id"],
            order["symbol"],
            order["side"],
            int(order["quantity"]),
            float(order["price"]),
            "NEW"
        )
    )

    connection.commit()

    cursor.close()
    connection.close()


if __name__ == "__main__":

    example_order = {
        "client_order_id": "ORD001",
        "symbol": "AAPL",
        "side": "BUY",
        "quantity": "100",
        "price": "190.50"
    }

    save_order(example_order)

    print("Order saved")