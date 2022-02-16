from socket import AF_INET, SOCK_STREAM, socket
from time import sleep

connection = socket(AF_INET, SOCK_STREAM)

addressPort = ('192.168.43.233', 9999)
sleep(1)
print(f'Connection Established')
connection.connect(addressPort)

while True:
    equation =  input('Enter Equation or quit: ')
    connection.send(equation.encode())
    sleep(0.5)
    if equation == 'quit':
        break
    answer = connection.recv(1024).decode()
    print(f'ans: {answer}')

print(f'Thank you')
connection.close()