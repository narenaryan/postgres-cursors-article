from psycopg2 import connect
import time


# Get this from ENV variables or configuration store
config = {
    "host": "db",
    "dbname": "dvdrental",
    "user": "postgres",
    "password": "mypassword",
    "port": "5432"
}

CLIENT_PAGINATION_LIMIT = 200
SERVER_PAGINATION_LIMIT = 500

def main():
    sql_query = 'SELECT * FROM film'
    with connect(**config) as conn:
        with conn.cursor("film") as cur:
            # This fetches only 200 records from DB as batches
            # If you don't specify, the default value is 2000
            cur.itersize = 200
            cur.execute(sql_query)

            for row in cur:
                print(row) # Use row

if __name__ == "__main__":
    main()
