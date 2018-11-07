#!/usr/bin/python

# This program iterates through an IP Address list and execute a specific command in the servers. 

import os

# Replace the 'xxx's with the IP Address range.

ip_list = ["xxx.xxx.xxx.xxx", "xxx.xxx.xxx.xxx"]

command = "cat /etc/passwd"

for ip in ip_list:
    os.system("ssh root" + "@" + ip + " '" + command + "'")
