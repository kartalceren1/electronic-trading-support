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

    # Get all orders
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

    # Count total orders
    cursor.execute(
        """
        SELECT COUNT(*)
        FROM orders
        """
    )

    total_orders = cursor.fetchone()[0]

    # Count filled orders
    cursor.execute(
        """
        SELECT COUNT(*)
        FROM orders
        WHERE status='FILLED'
        """
    )

    filled = cursor.fetchone()[0]

    # Count rejected orders
    cursor.execute(
        """
        SELECT COUNT(*)
        FROM orders
        WHERE status='REJECTED'
        """
    )

    rejected = cursor.fetchone()[0]

    # Get incidents
    cursor.execute(
        """
        SELECT order_id,
               incident_type,
               severity,
               description
        FROM incidents
        """
    )

    incidents = cursor.fetchall()
    print(incidents)

    cursor.close()
    connection.close()

    return render_template(
        "dashboard.html",
        orders=orders,
        total_orders=total_orders,
        filled=filled,
        rejected=rejected,
        incidents=incidents
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
