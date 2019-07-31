#!/usr/bin/python3

import os

# Replace the 'xxx's with the IP Address range.

ip_list = ["xxx.xxx.xxx.xxx", "xxx.xxx.xxx.xxx"]

command = "cat /etc/passwd"

for ip in ip_list:
    os.system("ssh root" + "@" + ip + " '" + command + "'")
