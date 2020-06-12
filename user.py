from database import connectionFromPool


class User:
    def __init__(self, first_name, email, last_name, id):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    def __repr__(self):
        return "<User {}>".format(self.email)

    def save_to_db(self):
        with connectionFromPool() as connection:
            with connection.cursor() as cursor:
                cursor.execute('INSERT INTO USERS(email,first_name,last_name) VALUES(%s,%s,%s)',
                               (self.email, self.first_name, self.last_name))

    @classmethod
    def load_from_db_by_email(cls, email):
        with connectionFromPool() as connection:
            with connection.cursor() as cursor:
                cursor.execute('select * from users where email=%s', (email,))
                user_data = cursor.fetchone()
                return cls(user_data[1], user_data[2], user_data[3], user_data[0])
