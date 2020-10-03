import socket

#Exercise 1: Change the socket program socket1.py to prompt the user for the URL so it can read any web page. 
# You can use split('/') to break the URL into its component parts so you can extract the host name for the socket connect call. 
# Add error checking using try and except to handle the condition where the user enters an improperly formatted or non-existent URL.

url = input("What url would you like to check? ")

print(url[:7])

#check integrity of link
if url[:7] != "http://" and url[:8] != "https://":
    print("Not a valid URL")
    exit()

#split url up into different parts for using
host = url.split("/")[2]

#make connection
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host, 80))
cmd = 'GET ' +url+ ' HTTP/1.0\r\n\r\n'
print(cmd)
mysock.send(cmd.encode())

charCounter=0

# Exercise 2: Change your socket program so that it counts the number of characters it has received and stops displaying any text after it has shown 3000 characters. 
# The program should retrieve the entire document and count the total number of characters and display the count of the number of characters at the end of the document.

#read data from website
byteStr= ''.encode()
while True:
    data = mysock.recv(3000)
    data.decode()
    if len(data) < 1:
        break
    byteStr += data

byteStr = byteStr.decode()

print(byteStr[:3000], "\nTotal Number of Bytes:", len(byteStr))

mysock.close()