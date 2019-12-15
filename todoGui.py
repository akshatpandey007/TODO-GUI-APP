import PySimpleGUI as sg

sg.change_look_and_feel('Dark Blue 3')


def pop(values):
    sg.popup(values)


def IntroForm():
    # defining layout of intro form
    layout = [[sg.Text("Hello, There...")],
              [sg.Button('Login'), sg.Button('Signup'), sg.Button('Exit')]]
    window = sg.Window('Window Title', layout)
    event = window.read()
    window.close()
    del window
    # options
    if event[0] == 'Login':
        return 1
    elif event[0] == 'Signup':
        return 2
    elif event[0] == 'Exit' or event[0] == 'None':
        return 3


def SignUpForm():
    layout = [[sg.Text('SignUp')],
              [sg.Text('FullName : '), sg.Input("name")],
              [sg.Text('UserId : '), sg.Input("userId")],
              [sg.Text('Password : '), sg.Input("password")],
              [sg.Button('Submit')]]
    window = sg.Window('SignUp Form', layout)
    event = window.read()
    window.close()
    del window
    return event


def LoginForm():
    layout = [[sg.Text('Login')],
              [sg.Text('UserId : '), sg.Input("userId")],
              [sg.Text('Password : '), sg.Input("password")],
              [sg.Button('Submit')]]
    window = sg.Window('Login', layout)
    event = window.read()
    window.close()
    del window
    return event


def todoGui(name):
    ls = (
        'Add a new task',
        "Show the number of tasks",
        "Delete a task by number",
        "Show all the tasks",
        "Quit",
        "LogOut",
        "Themes"
    )
    layout = [[sg.Text('Hii '+name)],
              [sg.Listbox(values=ls, size=(35, 8))],
              [sg.Button('submit')]
              ]
    window = sg.Window(
        'Window Title', default_element_size=(40, 1)).Layout(layout)
    event = window.read()
    event = event[1][0][0]
    event = ls.index(event)
    window.close()
    del window
    return event


def addTaskGui(name):
    layout = [[sg.Text('Hi '+name+"\n")],
              [sg.Text('ADD TASK')],
              [sg.Input("")],
              [sg.Button('Submit')]]
    window = sg.Window('add_task', layout)
    event = window.read()
    event = event[1][0]
    window.close()
    del window
    return event


def noTaskGui(name, warning):
    warn = sg.Text(warning)
    layout = [[warn],
              [sg.Text('hi '+name+', Enter the number of task')],
              [sg.Input("")],
              [sg.Button('Submit')]]
    window = sg.Window('Task at number', layout)
    event = window.read()
    event = event[1][0]
    window.close()
    del window
    return event


def showTasksGui(name, ls):
    l = ['']*(len(ls)+1)
    j = 0
    for i in ls:
        alpha = str(i[0])+") "+str(i[1])+"             ....."+str(i[2])
        l[j] = [sg.Text(alpha)]
        j += 1
        if j == len(ls):
            break
    l[len(ls)] = [sg.Button('Ok')]
    window = sg.Window('Tasks', l)
    event = window.read()
    window.close()
    del window


def theme(name):
    ls = (
        "Dark Blue 3",
        "Dark Blue 1",
        "Dark Blue 2",
    )
    layout = [[sg.Text('Hii '+name)],
              [sg.Listbox(values=ls, size=(35, 8))],
              [sg.Button('submit')]
              ]
    window = sg.Window(
        'Themes', default_element_size=(40, 1)).Layout(layout)
    event = window.read()
    event = event[1][0][0]
    sg.change_look_and_feel(event)
    window.close()
    del window
    return event
