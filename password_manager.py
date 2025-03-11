import hashlib
import getpass

password_manager = {}

def create_account ():
    username =  input("Enter your username: ")
    password = getpass.getpass("Set up password: ")
    hash_pass = hashlib.sha256(password.encode()).hexdigest()
    password_manager[username] = hash_pass

    print("Account created successfully...")

def login ():
    username = input("username: ")
    password = getpass.getpass("Password: ")
    hash_pass = hashlib.sha256(password.encode()).hexdigest()
    if username in password_manager.keys() and password_manager[username] == hash_pass:
        print("Login successful...")

    else:
        print("Invalid information")



def main():
    while True:
        print("\n1. Create a new account \n2. Login \n3. exit")
        choice  = int(input("Enter your choice: "))

        if choice == 1:
            create_account()
        elif choice == 2:
            login()
        elif choice == 3:
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()