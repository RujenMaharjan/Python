import os


from Sub import *
if not os.path.exists("Students.txt"):
    open("Students.txt","w").close()

question=input("Do you have account (y/n):")
if question=="y" or question=="Y" or question=="Yes" or question=="yes":
    print("Welcome please complete our login procedure")
    login.login()
elif question=="n" or question=="N" or question=="No" or question=="no":
    print("Welcome please complete our registration procedure")
    register.register()
else:
    print("Invalid input")
    exit()