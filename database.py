from psycopg2 import pool

connectionPool = pool.SimpleConnectionPool(1,
                                           1,
                                           dbname="learning",
                                           user="postgres",
                                           password="postgres",
                                           host="localhost",
                                           port="5432")


class connectionFromPool:
    def __init__(self):
        self.connection = None;

    def __enter__(self):
        self.connection = connectionPool.getconn()
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection_pool.getconn(self.connection)
