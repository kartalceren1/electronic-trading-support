def search_logs(order_id):

    file = open(
        "../logs/trading.log",
        "r"
    )

    lines = file.readlines()

    file.close()

    matches = []

    for line in lines:

        if order_id in line:
            matches.append(line.strip())

    return matches


def classify_incident(logs):

    summary = {
        "type": "Unknown",
        "cause": "Unknown"
    }

    for log in logs:

        if "rejected" in log:
            summary["type"] = "Order Rejection"
            summary["cause"] = "Exchange rejected order"

        elif "Connection reset" in log:
            summary["type"] = "Connectivity Issue"
            summary["cause"] = "Exchange connection failure"

        elif "Malformed FIX" in log:
            summary["type"] = "FIX Parsing Error"
            summary["cause"] = "Missing FIX tag"

    return summary


if __name__ == "__main__":

    logs = search_logs("ORD002")

    report = classify_incident(logs)

    print(report)