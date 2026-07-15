from flask import Flask, render_template
from database import get_connection


app = Flask(
    __name__,
    template_folder="../templates"
)


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

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM orders
        """
    )

    total_orders = cursor.fetchone()[0]

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM orders
        WHERE status='FILLED'
        """
    )

    filled = cursor.fetchone()[0]

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM orders
        WHERE status='REJECTED'
        """
    )

    rejected = cursor.fetchone()[0]

    cursor.close()
    connection.close()

    return render_template(
        "dashboard.html",
        orders=orders,
        total_orders=total_orders,
        filled=filled,
        rejected=rejected
    )


if __name__ == "__main__":
    app.run(debug=True)
