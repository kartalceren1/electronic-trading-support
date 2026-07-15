from database import get_connection


def find_missing_executions():

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    SELECT client_order_id, symbol, status
    FROM orders
    WHERE status = 'NEW'
    """

    cursor.execute(query)

    orders = cursor.fetchall()

    cursor.close()
    connection.close()

    return orders


if __name__ == "__main__":

    missing_orders = find_missing_executions()

    if not missing_orders:
        print("No incidents found.")

    else:
        print("Missing Execution Incidents:")

        for order in missing_orders:
            print(f"""
            ------------------------
            Incident Type : Missing Execution
            Order ID      : {order[0]}
            Symbol        : {order[1]}
            Status        : {order[2]}
            ------------------------
            """)