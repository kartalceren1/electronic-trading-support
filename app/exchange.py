import time


def send_order(order, reject=False):
    if reject:
        return {
            "status": "REJECTED",
            "reason": "Invalid price",
            "order_id": order["client_order_id"]
        }

    print("Exchange accepted order")

    time.sleep(2)

    print("Execution report received")

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
