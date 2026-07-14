import psycopg2


def get_connection():
    connection = psycopg2.connect(
        host="localhost",
        database="trading_support",
        user="postgres",
        password="password123",
        port="5432"
    )

    return connection


if __name__ == "__main__":
    connection = get_connection()
    print("Connected to PostgreSQL")
    connection.close()
