#Use socket in Python to simulate a webbrowser
#https://docs.python.org/3/library/socket.html

import socket

#AF_INET is telling socket to use IPv4
#SOCK_STREAM represents the socket TYPE, ***TCP*** in this case
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))

#GET request in the HTTP Header
cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode() #encode changes UNICODE to UTF-8
mysock.send(cmd)

while True:
    data = mysock.recv(512) # receive up to 512 characters
    if len(data) < 1:
        break
    print(data.decode()) # decode() converts from UTF-8 -> unicode

mysock.close()