# import pymysql
from mysql.connector import connect, Error
from config import host, user, password, db_name


# connection = pymysql.connect(
#     host = host,
#     port = 3306,
#     user = user,
#     password = password,
#     database = db_name,
#     cursorclass = pymysql.cursors.DictCursor)

# async def cmd_staer_db(chat_id):
#     try:
#         with connect(
#             host=host,
#             user="root",
#             password=password,
#             database=db_name
#         ) as connection:
#             with connection.cursor() as cursor:
#                 user = f"SELECT * FROM bot_table WHERE chat_id = {chat_id}"
#                 cursor.execute(user)
#                 if not user:
#                     add_user = f"INSERT INTO bot_table (chat_id) VALUES {chat_id}"
#                     cursor.execute(add_user)
#                     connection.commit()
#             print(connection)
#     except Error as e:
#         print(e)
    


# async def cmd_staer_db(chat_id):
#     user = f"SELECT * FROM bot_table WHERE chat_id = {chat_id}"
#     cursor.execute(user)
#     if not user:
#         add_user = f"INSERT INTO bot_table (chat_id) VALUES {chat_id}"
#         cursor.execute(add_user)
#         connection.commit()
# class Database:
#     def __init__(self):
#         self.connection = pymysql.connect(
#             host = host,
#             port = 3306,
#             user = user,
#             password = password,
#             database = db_name,
#             cursorclass = pymysql.cursors.DictCursor
#         )
#         self.cursor = self.connection.cursor()
    
#     def user_exists(self, chat_id):
#         with self.connection:
#             result = self.cursor.execute("SELECT * FROM `bot_table` WHERE chat_id = ?;", (chat_id))
#             return bool(len(result))
    
#     def add_user(self, chat_id):
#         with self.connection:
#             return self.cursor.execute("INSERT INTO `bot_table` (chat_id) VALUES (?);", (chat_id))