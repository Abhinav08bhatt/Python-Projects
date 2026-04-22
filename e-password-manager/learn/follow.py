'''
follow through the video file 
...as idk how to make a password manager, so learning in this one and will create my own in main.py
'''
'''
modules
pip install cryptography
'''
from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open ("e-password-manager/learn/key.key","wb") as key_file:
        key_file.write(key)

def load_key():
    file = open("e-password-manager/learn/key.key","rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("What is the master password? : ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

def view():
    with open("e-password-manager/learn/password.txt",'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            name,pwd = data.split("|")
            print(f"name = {name} | pwd : {fer.decrypt(pwd.encode())}")

def add():
    name = input("account name : ")
    pwd = input("password : ")

    with open("e-password-manager/learn/password.txt",'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
    

while True:
    mode = input("Would you like to add a new password or view existing ones (view,add,q to quit) ? : ").lower()
    if mode == "q":
        break

    elif mode == "view":
        view()

    elif mode == "add":
        add()

    else:
        print("Invalid mode...")
        continue