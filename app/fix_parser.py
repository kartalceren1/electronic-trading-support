def parse_fix_message(message):
    fields = {}

    parts = message.split("|")

    for part in parts:
        if "=" in part:
            tag, value = part.split("=")
            fields[tag] = value

    order = {
        "message_type": fields.get("35"),
        "client_order_id": fields.get("11"),
        "symbol": fields.get("55"),
        "side": fields.get("54"),
        "quantity": fields.get("38"),
        "price": fields.get("44")
    }

    return order


fix_message = "8=FIX.4.2|35=D|11=ORD001|55=AAPL|54=1|38=100|44=190.50|"

order = parse_fix_message(fix_message)

print(order)
