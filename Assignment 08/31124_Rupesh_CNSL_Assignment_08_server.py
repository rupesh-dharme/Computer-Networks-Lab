from socket import AF_INET, SOCK_DGRAM, socket
from time import perf_counter, sleep

server = socket(AF_INET, SOCK_DGRAM)

addressPort = ('', 9999)
server.bind(addressPort)
print(f'Server Binded')
print('Waiting for data...')
buffer, address = server.recvfrom(1024)
sleep(1)
data = buffer.decode()
print(data)

with open('recieved.mp4', 'wb') as file:
    print('Recieving',end = '')
    while True:
        data, address = server.recvfrom(65000)
        if not data:
            break
        sleep(1)
        file.write(data)
        print('.', end = '')
print('File recieved')

server.close()