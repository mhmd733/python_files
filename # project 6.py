# project 6 not fnisht
from cryptography import fernet
def write_key ():
    key = fernet.generate_key()
    with open("key.key","wd") as key_file :
        key_file.write(key)
def loud_key():
    file = open("key.key","rb")
    key = file.read()
    file.close
    return key 

master_pwd = input("What is the master password? : ")
key = loud_key() + master_pwd.encode
fer = fernet(key)
def view ():
 with open ('password.txt','r') as f :
     for line in f.readlines():
         data = line.rstrip()
         user,passw = data.split('|')
         print("user:", user, "|" "password:", fer.decrypt(passw.encode() ).decode())
def add():
    name = input("Account name: ")
    pwd = input("Enter the password: ")
    with open('password.txt','a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
while True :
    mode = input(" Do you want to add a new password or see the passwords? (view or add or q to exit) : ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
         add ()
    else : 
        print("Invalid mode.")
        continue