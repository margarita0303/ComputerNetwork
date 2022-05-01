import socket

from threading import Thread
from datetime import datetime
import time


def listen_for_connections(server, clients):
    print('Waiting for connections...')
    while True:
        conn, address = server.recvfrom(1024)
        print(f'Connected with new client {address}')
        clients.append(address)


def server(host, port):
    print('Server running...')
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((host, port))
    clients = []
    listener = Thread(target=listen_for_connections, args=[server, clients])
    listener.start()
    while True:
        cur_time = str(datetime.now())
        time.sleep(1)
        for client in clients:
            server.sendto(cur_time.encode('utf-8'), client)


if __name__ == '__main__':
    host = input('Enter server host: ')
    port = int(input('Enter server port: '))
    server(host, port)
