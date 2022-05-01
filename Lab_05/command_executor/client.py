import socket

def client(serverHost, serverPort):
    # SOCK_STREAM means that it is a TCP socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((serverHost, serverPort))

    command = input('Enter command: ')
    client.sendall(command.encode('utf-8'))


if __name__ == '__main__':
    serverHost = input('Input server host: ')
    serverPort = int(input('Input server port: '))
    client(serverHost, serverPort)
