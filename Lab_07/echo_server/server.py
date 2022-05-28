import socket
import time
from random import uniform


def start_server(HOST, PORT):
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server.bind((HOST, PORT))
        print('Server running...')
        while True:
            data, addr = server.recvfrom(1024)
            pause = uniform(0, 1)
            if pause > 0.8:
                continue
            else:
                time.sleep(pause)
                data = data.decode('utf-8').upper().encode('utf-8')
                server.sendto(data, addr)

    except KeyboardInterrupt:
        server.close()


if __name__ == '__main__':
    print("Input HOST:")
    HOST = input()
    print("Input PORT:")
    PORT = input()
    start_server(HOST, int(PORT))
