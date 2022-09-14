#=====importing libraries===========
# Importing the date module to get todays date.
from datetime import date
# Importing the text file that contains the username and logins.
f = open('user.txt', 'r+')      
#====Login Section====
login_verified = True
while login_verified:
    print("Welcome to Task Manager! Please log in below.")
    username_login = input("Enter username: ")
    password_login = input("Enter password: ")
    for line in f: # The for loop to check the user login and using if functions to check if the input is the same as on file.
        split_line = line.split(", ")
        if split_line[0] == username_login and split_line[1].strip("\n") == password_login:
            print("Login succesfull")
            login_verified = False
        elif split_line[0] != username_login and split_line[1].strip("\n") == password_login:
            print("Username  is incorrect.")
        elif split_line[0] == username_login and split_line[1].strip("\n") != password_login:
            print("Password is incorrect")
        elif split_line[0] != username_login and split_line[1].strip("\n") != password_login:
            continue
        else:
            print("Username does not exist")
    f.seek(0)
f.close()
while True:
    if username_login == "admin": # Seperate menu for the admin user
        menu = input('''Select one of the following Options below
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my tasks
e - Exit
s - Statistics
: ''').lower()
        if menu == 'r': # This section is to add new users only admins can do so.
            if username_login == "admin":
                user = open('user.txt', 'a')
                new_username = input("Please enter a new username: ")
                new_password = input("Please enter a new password: ")
                new_password_confirmation = input("Please confirm password: ")
                split_line = line.split(", ")
                if split_line[0] != new_username and new_password == new_password_confirmation:
                    print("User created")
                    user.write(new_username + ", " + new_password + "\n")
                    user.close()
                elif split_line[0] == username_login:
                    print("Username already exist")
                elif split_line[0] != username_login and new_password != new_password_confirmation:
                    print("Passwords do not match!")
            else:
                print("Only admins can register a new user.") # An message to display if a non admin user tries to add a new user.
    
        elif menu == 'a': # This section is to addd a new task
            assigned_user = input("Enter the username: ")
            task_title = input("Enter the task title: ")
            task_description = input("Task description: ")
            print("Write your date as the following example: 05 April 2022") # Recommended a default date format 
            due_date = input("Due date: ")
            date_today = input("Today's date: ")
            with open('tasks.txt', 'a') as f:
                f.write(assigned_user+", "+task_title+", "+task_description+", "+due_date+", "+date_today+", "+"No"+"\n")
                f.close()

        elif menu == 'va': # This section is to view all tasks for all users
            f = open('tasks.txt', 'r')
            tasks = []
            for line in f:
                stripped_task = line.strip("\n")
                line_task = stripped_task.split(", ")
                tasks.append(line_task)
                print("""--------------------------------------------------------------------------------
Task:\t\t{}
Assigned to:\t\t{}
Date assigned:\t\t{}
Due Date:\t\t{}
Task Comlete?\t\t{}
Task Description:\n{}
--------------------------------------------------------------------------------""".format(line_task[1], line_task[0], line_task[3], line_task[4], line_task[5], line_task[2]))
            f.close()
        elif menu == 'vm': # This section is to view the task assigned to the user that is logged in.
            f = open('tasks.txt', 'r')
            tasks = []
            for line in f:
                stripped_task = line.strip("\n")
                line_task = stripped_task.split(", ")
                tasks.append(line_task)
                if username_login == line_task[0]:
                    print("""--------------------------------------------------------------------------------
Task:\t\t{}
Assigned to:\t\t{}
Date assigned:\t\t{}
Due Date:\t\t{}
Task Comlete?\t\t{}
Task Description:\n{}
--------------------------------------------------------------------------------""".format(line_task[1], line_task[0], line_task[3], line_task[4], line_task[5], line_task[2]))
                else:
                    print("User has no tasks.")
            f.close()
        elif menu == 's': # This section is only available
            if username_login == 'admin':
                task_file = open('tasks.txt', 'r')
                user_file = open('user.txt', 'r')
                task_file_len = len(task_file.readlines())
                user_file_len = len(user_file.readlines())
                print("""
Total tasks: {}
Total users: {}""".format(task_file_len, user_file_len))
            else:
                print("You don't have access sorry.")

        elif menu == 'e':
            print('Goodbye!!!')
            exit()

        else:
            print("Wrong selection, Please Try again")
    else: # This section is for non admin users
        menu = input('''Select one of the following Options below
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my tasks
e - Exit
: ''').lower()
        if menu == 'r':
            if username_login == "admin": # This section is to add new users only admins can do so.
                user = open('user.txt', 'a')
                new_username = input("Please enter a new username: ")
                new_password = input("Please enter a new password: ")
                new_password_confirmation = input("Please confirm password: ")
                split_line = line.split(", ")
                if split_line[0] != new_username and new_password == new_password_confirmation:
                    print("User created")
                    user.write(new_username + ", " + new_password + "\n")
                    user.close()
                elif split_line[0] == username_login:
                    print("Username already exist")
                elif split_line[0] != username_login and new_password != new_password_confirmation:
                    print("Passwords do not match!")
            else:
                print("Only admins can register a new user.") # An message to display if a non admin user tries to add a new user.
    
        elif menu == 'a': # This section is to addd a new task
            assigned_user = input("Enter the username: ")
            task_title = input("Enter the task title: ")
            task_description = input("Task description: ")
            print("Write your date as the following example: 05 April 2022") # Recommended a default date format 
            due_date = input("Due date: ")
            date_today = input("Today's date: ")
            with open('tasks.txt', 'a') as f:
                f.write(assigned_user+", "+task_title+", "+task_description+", "+due_date+", "+date_today+", "+"No"+"\n")
                f.close()

        elif menu == 'va': # This section is to view all tasks for all users
            f = open('tasks.txt', 'r')
            tasks = []
            for line in f:
                stripped_task = line.strip("\n")
                line_task = stripped_task.split(", ")
                tasks.append(line_task)
                print("""--------------------------------------------------------------------------------
Task:\t\t{}
Assigned to:\t\t{}
Date assigned:\t\t{}
Due Date:\t\t{}
Task Comlete?\t\t{}
Task Description:\n{}
--------------------------------------------------------------------------------""".format(line_task[1], line_task[0], line_task[3], line_task[4], line_task[5], line_task[2]))
            f.close()
        elif menu == 'vm': # This section is to view the task assigned to the user that is logged in.
            f = open('tasks.txt', 'r')
            tasks = []
            for line in f:
                stripped_task = line.strip("\n")
                line_task = stripped_task.split(", ")
                tasks.append(line_task)
                if username_login == line_task[0]:
                    print("""--------------------------------------------------------------------------------
Task:\t\t{}
Assigned to:\t\t{}
Date assigned:\t\t{}
Due Date:\t\t{}
Task Comlete?\t\t{}
Task Description:\n{}
--------------------------------------------------------------------------------""".format(line_task[1], line_task[0], line_task[3], line_task[4], line_task[5], line_task[2]))
                else:
                    print("User has no tasks.")
            f.close()

        elif menu == 'e':
            print('Goodbye!!!')
            exit()

        else:
            print("Wrong selection, Please Try again")
