from cryptography.fernet import Fernet
import os

def write_key():
    key = Fernet.generate_key()
    with open("e-password-manager/key.key", 'wb') as fk:
        fk.write(key)

def read_key():
    if not os.path.exists("e-password-manager/key.key"):
        write_key()
    with open("e-password-manager/key.key", "rb") as fk:
        return fk.read()

fernet = Fernet(read_key())

def create_master_pwd():
    master = input("CREATE MASTER PASSWORD : ")
    confirm = input("CONFIRM PASSWORD : ")

    if master != confirm:
        print("Passwords DO NOT match.\nTry again...\n")
        return create_master_pwd()

    encrypted_master = fernet.encrypt(master.encode()).decode()

    with open("e-password-manager/master.txt", "w") as fw:
        fw.write(encrypted_master)

    print("Master password created!\n")

def verify_master_pwd():
    with open("e-password-manager/master.txt", "r") as f:
        encrypted_master = f.read().strip()

    stored_master = fernet.decrypt(encrypted_master.encode()).decode()
    user_input = input("Enter MASTER PASSWORD : ")

    if user_input == stored_master:
        print("Access granted!\n")
        return True
    else:
        print("Incorrect master password.")
        return False

def look_up():
    if not os.path.exists("e-password-manager/master.txt"):
        print("No MASTER PASSWORD found. Create one now.\n")
        create_master_pwd()
    else:
        if not verify_master_pwd():
            exit()

def view():
    if not os.path.exists("e-password-manager/password.txt"):
        print("No passwords saved yet.\n")
        return

    with open("e-password-manager/password.txt", "r") as fr:
        for line in fr.readlines():
            data = line.rstrip()
            if "|" not in data:
                continue
            name, pwd = data.split("|")
            decrypted = fernet.decrypt(pwd.encode()).decode()
            print(f"Account: {name} | Password: {decrypted}")

def add():
    name = input("Account name : ")
    pwd = input("Password : ")
    encrypted = fernet.encrypt(pwd.encode()).decode()

    with open("e-password-manager/password.txt", 'a') as f:
        f.write(name + "|" + encrypted + "\n")

    print("Password added successfully!\n")


if __name__ == "__main__":
    look_up()

    while True:
        mode = input("Would you like to [add], [view], or [quit]? ").lower()

        if mode == "view":
            view()
        elif mode == "add":
            add()
        elif mode == "quit":
            print("Goodbye!")
            break
        else:
            print("Invalid selection.\n")
