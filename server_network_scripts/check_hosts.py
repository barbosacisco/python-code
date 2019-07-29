
import os

ip_addresses = [
    '192.168.8.1',
    '192.168.8.20',
    '192.168.8.90',
    '192.168.8.15',
    ]

for ip in ip_addresses:
    response = os.system('ping -c 1 ' + ip)
    if response == 0:
            print
            ip, 'is up'
    else:
            print
            ip, 'is down'
