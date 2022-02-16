from socket import socket
from time import sleep

s = socket()
host = ''
port = 9999
s.bind((host, port))
s.listen()
print("Listning...")
connection, address = s.accept()
print(f'connected to address {address}')

frames = int(connection.recv(1024).decode()) #No of frames to send
case = int(connection.recv(1024).decode()) #Case
print(f'Case chosen is {case}')

if case == 0: #No error case
    for i in range(1, frames+1):
        connection.send(str(i).encode())
        print('Frame sent.')
        sleep(1)
        ack = connection.recv(1024).decode()
        print('Acknowledgment recieved')
else: #Error case
    for i in range(1, frames+1):
        if i == 3:
            print("Frame sent.")
        else:
            connection.send(str(i).encode())
            print("Frame sent.")
            ack = int(connection.recv(1024).decode())
            if ack == -1:
                break
            print('Acknowledgment recieved', ack)
    for j in range(i-1, frames+1):
        connection.send(str(j).encode())
        print("Frame sent.")
        ack = int(connection.recv(1024).decode())
        print('Acknowledgment recieved', ack)

s.close()