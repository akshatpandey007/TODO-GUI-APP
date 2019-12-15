import sqlite3 as sq


class UserDataManage():
    def __init__(self):
        global con
        try:
            con = sq.connect('users.db')
            with con:
                cur = con.cursor()
                cur.execute(
                    "CREATE TABLE IF NOT EXISTS user(Id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, userid TEXT, userpassword TEXT)")
        except Exception:
            print('Unable to connect to User db')

    def insert_tasks(self, task):
        try:
            con = sq.connect('users.db')
            with con:
                cur = con.cursor()
                sql = "INSERT INTO user(name,userid, userpassword) VALUES (?,?,?)"
                cur.execute(sql, task)
                return True
        except Exception:
            return False

    def fetch_tasks(self):
        try:
            con = sq.connect('users.db')
            with con:
                cur = con.cursor()
                sql = "SELECT * FROM user"
                cur.execute(sql)
                return cur.fetchall()
        except Exception:
            return False
