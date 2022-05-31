import socket

def start_server(HOST, PORT):
    try:
        server_socket = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
    except Exception:
        print('Error. Cannot start server.')
        return
    print('Server is running')
    while True:
        client_request, address = server_socket.recvfrom(1024)
        client_request = client_request.decode('utf-8')
        print(f'Client request: {client_request}')
        response = client_request.upper().encode('utf-8')
        server_socket.sendto(response, address)
        print(f'Server: {response}')

if __name__ == '__main__':
    host = input("Input host name: ")
    port = input("Input port: ")
    start_server(host, int(port))
