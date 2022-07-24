import os
import getpass

if not os.path.exists("Students.txt"):
    open("Students.txt","w").close()

def register():
    username=input("Enter your username:")
    password=getpass.getpass("Enter password:")
    username=username.lstrip()
    username=username.rstrip()
    password=password.rstrip()
    password=password.rstrip()
    #checking if username pre exists in database
    if username in open("Students.txt").read():
        print("Sorry this username already exists")
        exit()
    confirm_password=getpass.getpass("Confirm password:")
    confirm_password=confirm_password.lstrip()
    confirm_password=confirm_password.rstrip()
    if password!=confirm_password:
        print("Incorrect passoword")
        exit()
    with open("Students.txt","a") as file:
        file.write(f"username:{username},password:{password}\n")
        exit()
        print("Registerd succesfully")

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

question=input("Do you have account (y/n):")
if question=="y" or question=="Y" or question=="Yes" or question=="yes":
    print("Welcome please complete our login procedure")
    login()
elif question=="n" or question=="N" or question=="No" or question=="no":
    print("Welcome please complete our registration procedure")
    register()
else:
    print("Invalid input")
    exit()