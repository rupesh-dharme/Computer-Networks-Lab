from socket import AF_INET, SOCK_DGRAM, socket
from time import sleep

client = socket(AF_INET, SOCK_DGRAM)
addressPort = ('192.168.43.233', 9999)
str = 'Hello world'
print('Sending data...')
client.sendto(str.encode(), addressPort)
sleep(1)
print(f'Sending file', end='')

with open('file.mp4', 'rb') as file:
    while True:
        data = file.read(65000)
        client.sendto(data, addressPort)
        sleep(1)
        print('.', end= '')
        if not data:
            break
print('File sent')

client.close()