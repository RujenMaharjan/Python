import getpass
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