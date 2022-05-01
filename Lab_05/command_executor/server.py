import socket
from os import system


def server(host, port):
    print('Server starting...')
    # SOCK_STREAM means that it is a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    conn, addr = server_socket.accept()
    print(f'Connected by {addr}')
    command = conn.recv(1024).decode('utf-8')
    print(f'Got command: {command}')
    system(command)
    conn.close()


if __name__ == '__main__':
    serverHost = input('Input server host: ')
    serverPort = int(input('Input server port: '))
    server(serverHost, serverPort)
