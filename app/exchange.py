import time

from app.order_updates import update_order_status


def send_order(order, reject=False):
    if reject:
        update_order_status(
            order["client_order_id"],
            "REJECTED"
        )

        return {
            "status": "REJECTED",
            "reason": "Invalid price",
            "order_id": order["client_order_id"]
        }

    print("Exchange accepted order")

    time.sleep(2)

    print("Execution report received")

    update_order_status(
        order["client_order_id"],
        "FILLED"
    )

    return {
        "status": "FILLED",
        "order_id": order["client_order_id"]
    }


if __name__ == "__main__":
    test_order = {
        "client_order_id": "ORD001",
        "symbol": "AAPL",
        "quantity": 100
    }

    result = send_order(test_order, reject=False)

    print(result)
