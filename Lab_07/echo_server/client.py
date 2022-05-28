import socket
from datetime import datetime
from time import time


def start_client(HOST, PORT):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.connect((HOST, PORT))
    client.settimeout(1)

    for i in range(1, 11):
        msg = f'Ping {i} {datetime.now()}'
        start = time()
        client.sendto(msg.encode('utf-8'), (HOST, PORT))
        try:
            data = client.recvfrom(1024)[0].decode('utf-8')
            rtt = time() - start
            print(data, '\nRTT =', rtt, 'seconds')
        except Exception:
            print('Request timed out\n')


if __name__ == '__main__':
    print("Input HOST:")
    HOST = input()
    print("Input PORT:")
    PORT = input()
    start_client(HOST, int(PORT)) 
