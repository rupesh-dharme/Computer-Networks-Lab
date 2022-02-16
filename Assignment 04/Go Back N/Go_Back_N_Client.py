from socket import socket
from time import sleep

connection = socket()
host = '192.168.43.233'
port = 9999
connection.connect((host, port))
print("Connected...")

frames = int(input("Enter number of frames to recieve from server: "))
connection.send(str(frames).encode())

case = input("Enter the case(Error:1 Normal:0): ")
connection.send(case.encode())

if case == '0': #No error case
    for i in range(1, frames+1):
        frame = connection.recv(1024).decode()
        print("Frame recieved.")
        connection.send(frame.encode())
        print("Acknowledgment sent.")
else: #Error case
    check = 1
    for i in range(1, frames+1):
        frame = int(connection.recv(1024).decode())
        print("Frame recieved.")
        if frame == check:
            connection.send(str(frame).encode())
            print("Acknowledgment sent.")
        else:
            connection.send('-1'.encode())
            break
        check+=1
    for i in range(check, frames+1):
        frame = int(connection.recv(1024).decode())
        print('Frame recieved.')
        connection.send(str(frame).encode())
        print('Acknowledgement sent.')

connection.close()