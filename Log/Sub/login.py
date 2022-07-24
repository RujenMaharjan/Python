import getpass
def login():
    username= input("Enter your username:")
    password= getpass.getpass("Enter your password:")
    username=username.rstrip()
    username=username.lstrip()
    password=password.rstrip()
    password=password.lstrip()
    login_success=False
    with open("Students.txt","r") as file:
        for line in file:
            uname= line.split(",")[0][9:]
            upass= line.split(",")[1][9:]
            uname=uname.lstrip()
            uname=uname.rstrip()
            upass=upass.lstrip()
            upass=upass.rstrip()
            if username==uname and password==upass:
                login_success= True

            if login_success== True:
                print(f"Welcome to the system {username}")
            elif username!=uname:
                print(f"{username} has not been registerdregisterd")
            elif password!=upass:
                print(f"Incorrect password")
            else:
                print("Invalod input")