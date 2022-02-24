from email import message
import hashlib
import sqlite3
from hashlib import md5

from sqlalchemy import false
from ..models import user_model

class UserAction:

    def __init__(self, db_connection):
        self.db_connection = db_connection
    # tìm hiểu về bcrypt
    def login(self, user: user_model.User):
        conn = self.db_connection;
        cursor = conn.cursor()
        sql = """
            SELECT *
            FROM tbl_user
            WHERE username LIKE %s AND password LIKE %s
        """
        hashed = md5(user.password.encode()).hexdigest()
        print(hashed)
        cursor.execute(sql, (user.username, hashed))
        row = cursor.fetchone()
        if row == None:
            # sai user name hoặc password
            return 'Invalid username or password', 401
        
        authenticated_user = user_model.User(
            user_id=row[0],
            username=row[1],
            role=row[3]
        )
        return authenticated_user, 200

    def register(self, user: user_model.User):
        conn = self.db_connection;
        cursor = conn.cursor()
        try:
            sql = """
                INSERT INTO tbl_user(username,password) VALUE(%s,%s)
            """
            hashed = md5(user.password.encode()).hexdigest()
            val =(user.username,hashed)
            cursor.execute(sql,val)
            conn.commit()
        except Exception as e:
            return 'Fail ', 401
        return "success", 200
