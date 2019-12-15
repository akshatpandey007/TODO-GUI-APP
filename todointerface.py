import db as dbase
from datetime import datetime
import userdb
import todoGui as ta
import os
from os import path

# -----options----
# 'Add a new task',
# "Show the number of tasks",
# "Delete a task by number",
# "Show all the tasks",
# "Quit",
# "LogOut"
# "Theme"

f_state = 'savestate.txt'


def add_task(name, privatedb):
    try:
        task = ta.addTaskGui(name)
        task = [task, str(datetime.now())]
        if privatedb.insert_tasks(task):
            ta.pop("Data inserted succesfully!!")
        else:
            ta.pop("Data can not be inserted")
    except Exception:
        ta.pop("Some Unusual Exception Ocuured")


def noTask(name, privatedb):
    try:
        tasks = privatedb.fetch_tasks()
        if tasks == False:
            ta.pop('Database can not be fetched sorry')
        else:
            ta.pop('Hi '+name + '\n number of tasks are :' + str(len(tasks)))
    except Exception:
        ta.pop('Some unusual Exception ocuured!!')


def delTask(name, privatedb):
    warning = "Warning:While deleting enter the correct ID number and not the sequence number"
    try:
        id = ta.noTaskGui(name, warning)
        sequence = int(id)
        dele = privatedb.delete_tasks(sequence)
        if dele == False:
            ta.pop('Task can not be deleted')
        else:
            ta.pop('Task deleted successfully!!')
    except Exception:
        ta.pop('Some unusual Exception ocuured!!')


def showTasks(name, privatedb):
    try:
        tasks = privatedb.fetch_tasks()
        if tasks == False:
            ta.pop('Database can not be fetched sorry')
        else:
            ta.showTasksGui(name, tasks)
    except Exception:
        ta.pop('Some unusual Exception ocuured!!')


def todo(name, userid, privdb):
    privatedb = dbase.DataManage(privdb)
    while True:
        ch = ta.todoGui(name)
        if ch == 0:
            add_task(name, privatedb)
        elif ch == 1:
            noTask(name, privatedb)
        elif ch == 2:
            delTask(name, privatedb)
        elif ch == 3:
            showTasks(name, privatedb)
        elif ch == 4:
            exit(1)
        elif ch == 5:
            del name
            del userid
            del privdb
            del privatedb
            if path.exists(f_state):
                os.remove(f_state)
            main()
        elif ch == 6:
            # TODO change theme function
            ta.theme(name)
        else:
            ta.pop('wrong choice!!')


def loginAuth(user):
    try:
        flag_user = False
        users_db = ud.fetch_tasks()
        if users_db == False:
            ta.pop('Unable to Log in')
        else:
            for user_in_db in users_db:
                name = user_in_db[1]
                userid = user_in_db[2]
                password = user_in_db[3]
                if (userid == user[1]):
                    flag_user = True
                    break
            if flag_user:
                if not password == user[2]:
                    ta.pop('Invalid Password')
                else:
                    fState = open(f_state, "w")
                    fState.write(name+"@,@"+userid+"@,@"+password)
                    fState.close()
                    privdb = userid+name+'.db'
                    todo(name, userid, privdb)
            else:
                ta.pop('User does not exist, please sighnup')
                signup()

    except Exception:
        exit(1)


def signup():
    try:
        user = ta.SignUpForm()
        user = user[1]
        user = [user[0], user[1], user[2]]
        flag = 0
        users_db = ud.fetch_tasks()
        for user_in_db in users_db:
            name = user_in_db[1]
            userid = user_in_db[2]
            password = user_in_db[3]
            if (userid == user[1]):
                flag = 1
                break
        if flag == 1:
            ta.pop('User Id already Exists!!')
            main()
        else:
            if ud.insert_tasks(user) == False:
                ta.pop('Unable to sign up!!')
            else:
                loginAuth(user)
    except Exception:
        ta.pop('Something Unexpected Happened in SignUp Auth.')


def main():
    global ud
    ud = userdb.UserDataManage()
    if not(path.exists(f_state)):
        ch = ta.IntroForm()
        if ch == 1:
            user = ta.LoginForm()
            user = user[1]
            user = ['', user[0], user[1]]
            loginAuth(user)
        elif ch == 2:
            signup()
        elif ch == 3:
            exit(1)
    else:
        fState = open(f_state, "r")
        user = fState.readline()
        fState.close()
        user = user.split('@,@')
        loginAuth(user)


main()
