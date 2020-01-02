from user import User


my_user = User('zamoo','zamo@gmail.com','tery',None)

my_user.save_to_db()

user_from_db = User.load_from_db_by_email('thendo@gmail.com')

print(user_from_db)
my_user.save_to_db()

