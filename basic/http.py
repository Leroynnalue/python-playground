import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = 'data.prte.org'
PORT = 80

mysocket.connect((HOST, PORT))
request = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysocket.send(request)

number_of_characters = 512

while True:
    data = mysocket.recv(number_of_characters)
    if len(data) <  1 :
        break
    print(data.decode())

mysocket.close()