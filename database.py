from psycopg2 import pool

connection_pool = pool.SimpleConnectionPool(1,
                                            1,
                                            dbname="learning",
                                            user="postgres",
                                            password="postgres",
                                            host="localhost",
                                            port="5432")


class connectionFromPool:
    def __init__(self):
        self.connection = None

    def __enter__(self):
        self.connection = connection_pool.getconn()
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection_pool.putconn(self.connection)
