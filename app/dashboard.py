from flask import Flask
from database import get_connection


app = Flask(__name__)


@app.route("/")
def home():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT client_order_id,
               symbol,
               quantity,
               price,
               status
        FROM orders
        """
    )

    orders = cursor.fetchall()

    cursor.close()
    connection.close()


    html = """
    <h1>Electronic Trading Support Dashboard</h1>

    <h2>Orders</h2>

    <table border="1">

    <tr>
        <th>Order ID</th>
        <th>Symbol</th>
        <th>Quantity</th>
        <th>Price</th>
        <th>Status</th>
    </tr>
    """

    for order in orders:

        html += f"""
        <tr>
            <td>{order[0]}</td>
            <td>{order[1]}</td>
            <td>{order[2]}</td>
            <td>{order[3]}</td>
            <td>{order[4]}</td>
        </tr>
        """

    html += "</table>"

    return html


if __name__ == "__main__":

    app.run(debug=True)