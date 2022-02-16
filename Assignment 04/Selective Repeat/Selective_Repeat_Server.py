from socket import socket
from time import sleep

server = socket()
server.bind(('', 9999))
print("Listening...")
server.listen()
connection, address = server.accept()
print("Connection established", address)
sleep(1)

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
connection.send(str(len(array)).encode())

for i in array:
    connection.send(str(i).encode())
    print(f'Sending packet {i}')
    sleep(1)

index = int(connection.recv(1024).decode())
print("Resending lost frame...")
connection.send(str(array[index]).encode())
print('Lost frame sent')
sleep(2)
print(f'Frames sent: {array}')

server.close()
