#!/usr/bin/python
import subprocess
print("This script will support only IPv4 address")
print("If your IP address is starting from 127.0.0.1 , then only enter: 127.0.0. , If your IP address is starting from 192.168.10.1 , then only enter: 192.168.10. ")
print("###############################")
sip_addr=raw_input("Enter IP Address: ")
ra_a=int(raw_input("Enter Start Range Of IP Address: "))
ra_b=int(raw_input("Enter End Range Of IP Address (Should be higher than start range but less than 255): "))
for ping in range(ra_a,ra_b):
    ip_address = sip_addr + str(ping)
    res = subprocess.call(['ping', '-c', '3', ip_address])
    if res == 0:
        print "ping IP", ip_address, ""
    elif res == 2:
        print "no response from", ip_address
    else:
        print "ping IP", ip_address, "failed!"
