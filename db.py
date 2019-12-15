import sqlite3 as sq


class DataManage(object):
    def __init__(self, db):
        global con
        self.dbase = db
        try:
            con = sq.connect(db)
            with con:
                cur = con.cursor()
                cur.execute(
                    "CREATE TABLE IF NOT EXISTS task(Id INTEGER PRIMARY KEY AUTOINCREMENT, todo TEXT, time TEXT)")
        except Exception:
            print('Unable to connect to db')

    def insert_tasks(self, task):
        try:
            con = sq.connect(self.dbase)
            with con:
                cur = con.cursor()
                sql = "INSERT INTO task(todo, time) VALUES (?,?)"
                cur.execute(sql, task)
                return True
        except Exception:
            print(Exception)
            return False

    def fetch_tasks(self):
        try:
            con = sq.connect(self.dbase)
            with con:
                cur = con.cursor()
                sql = "SELECT * FROM task"
                cur.execute(sql)
                return cur.fetchall()
        except Exception:
            return False

    def delete_tasks(self, id):
        try:
            con = sq.connect(self.dbase)
            with con:
                cur = con.cursor()
                sql = "DELETE FROM task WHERE id=?"
                cur.execute(sql, [id])
                con.commit()
                cur.close()
                return True
        except Exception:
            return False
