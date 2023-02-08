import getpass
import hashlib
import os


print ("Passwordmanager made by Fast")
print ("Visit https://github.com/nathanfast")
print ("")

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(password, hashed_password):
    return hash_password(password) == hashed_password

def verify_master_password():
    try:
        with open("master_password.txt", "r") as file:
            hashed_password = file.read()
    except FileNotFoundError:
        print("Master password file not found.")
        return False
    master_password = getpass.getpass("Enter your master password: ")
    return verify_password(master_password, hashed_password)

def create_master_password():
    master_password = getpass.getpass("Enter a new master password: ")
    hashed_password = hash_password(master_password)
    with open("master_password.txt", "w") as file:
        file.write(hashed_password)
    print("Master password has been created.")

def change_master_password():
    if not verify_master_password():
        return
    master_password = getpass.getpass("Enter a new master password: ")
    hashed_password = hash_password(master_password)
    with open("master_password.txt", "w") as file:
        file.write(hashed_password)
    print("Master password has been changed.")

def view_passwords():
    if not verify_master_password():
        return
    try:
        with open("passwords.txt", "r") as file:
            content = file.read()
    except FileNotFoundError:
        print("Password file not found.")
        return
    print(content)

def add_password():
    if not verify_master_password():
        return
    website = input("Enter the website: ")
    password = getpass.getpass("Enter the password: ")
    try:
        with open("passwords.txt", "a") as file:
            file.write(website + " " + password + os.linesep)
    except FileNotFoundError:
        with open("passwords.txt", "w") as file:
            file.write(website + " " + password + os.linesep)
    print("Password has been added.")

def menu():
    print("Welcome to the password manager.")
    while True:
        print("What would you like to do?")
        print("1. Create master password")
        print("2. Change master password")
        print("3. View passwords")
        print("4. Add password")
        print("5. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            create_master_password()
        elif choice == "2":
            change_master_password()
        elif choice == "3":
            view_passwords()
        elif choice == "4":
            add_password()
        elif choice == "5":
            break

if __name__ == "__main__":
    menu()
