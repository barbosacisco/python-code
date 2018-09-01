#!/usr/bin/python

"""

 This program iterate through an IP Address list,
 and execute a specific command in the servers. 

"""


import os



ip_list = ["xxx.xxx.xxx.xxx" , "xxx.xxx.xxx.xxx"] # Change it for the IP Addresses of your servers. 

user = "root" # Define the server user. 

command = "cat /etc/passwd" # Define the command to be executed in the remote server. 



for ip in ip_list:
	os.system("ssh" + user + " + "@" + ip + " '" + command + "'")



"""

To get this program working you may have your servers able to be accessed via ssh-key. 
Configure your ssh service accordinly. 


"""
