import socket


def client(serverHost, serverPort):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
        client.sendto(b'Connect', (serverHost, serverPort))
        while True:
            tm = client.recvfrom(1024)[0]
            print(tm.decode('utf-8')) 

if __name__ == '__main__':
    serverHost = input('Input server host: ')
    serverClient = int(input('Input server port: '))
    client(serverHost, serverClient)
