from socket import AF_INET, SOCK_STREAM, socket
from time import sleep

def calculate(equation):
    answer = eval(equation)
    return str(answer)

server = socket(AF_INET, SOCK_STREAM)
addressPort = ('', 9999)
sleep(1)
print(f'Server created')
server.bind(addressPort)
print(f'Server binded')
sleep(1)
server.listen(5)
connection, address = server.accept()
print(f'Server connected to address {address}')
sleep(1)

while True:
    equation = connection.recv(1024).decode()
    if equation.strip() == 'quit':
        break
    else:
        print(f'Calculating...')
        sleep(1)
        print('Answer sent')
        answer = calculate(equation.strip())
        connection.send(answer.encode())


print(f'Thank you!')
server.close()