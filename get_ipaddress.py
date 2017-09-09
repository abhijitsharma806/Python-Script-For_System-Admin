#!/usr/bin/python
import socket
socket.gethostbyname(socket.gethostname())
#Print Host Name
print("System Hostname is: ")
print(socket.gethostname())
#Print IP Address
print("System IPAddress is: ")
print(socket.gethostbyname(socket.gethostname()))
