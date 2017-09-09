#!/usr/bin/python
import os
import crypt
# Default Password fot your user
user_name=raw_input("Enter Your Username: ")
user_pass=raw_input("Enter Your Password: ")
encPass = crypt.crypt(user_pass,"22")
os.system("useradd -p "+encPass+" "+user_name)
