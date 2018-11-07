# This program iterates through an IP Address list and execute a specific command in the servers.

import os

ip_list = ["xxx.xxx.xxx.xxx", "xxx.xxx.xxx.xxx"]

command = "cat /etc/passwd"

for ip in ip_list:
    os.system("ssh root" + "@" + ip + " '" + command + "'")
