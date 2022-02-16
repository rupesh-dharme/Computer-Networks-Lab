from socket import socket
from time import sleep

client = socket()
print("Connecting...")
sleep(3)
client.connect(('192.168.43.233', 9999))
print("Connected to server.")

frames = int(client.recv(1024).decode())
print(f'Server sending {frames} frames')
sleep(1)

array = []

for i in range(frames):
    frame = int(client.recv(1024).decode())
    print(f'Frame recieved {frame}')
    array.append(frame)

array[4] = -1
print(f'Frames recieved: {array}')

for i in array:
    if i == -1:
        client.send(str(i).encode())
        print('Requesting server to resend frame...')
        sleep(2)
        array[array.index(-1)] = int(client.recv(1024).decode())
        print('Recieved lost frame')
        sleep(1)

print(f'Frames recieved: {array}') 

client.close()