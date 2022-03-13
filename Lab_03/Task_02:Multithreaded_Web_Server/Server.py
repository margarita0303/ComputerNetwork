import socket
from threading import Thread

HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
HDRS_404 = 'HTTP/1.1 404 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
HOST = "127.0.0.1"
PORT = 1500
encoding_format = 'utf-8'


def start_server():
    try:
        server = socket.create_server((HOST, PORT))
        server.listen(4)
        while True:
            conn, address = server.accept()
            thread = Thread(target=on_new_client, args=(conn, address))
            thread.start()

    except KeyboardInterrupt:
        server.close()
        print('Server is closed.')


def on_new_client(conn, connection):
    request = conn.recv(1024).decode(encoding_format)
    conn.send(load_page_from_request(request))
    conn.close()


def load_page_from_request(request):
    path = 'Pages' + request.split(' ')[1]
    try:
        with open(path, 'rb') as file:
            response = file.read()
        return HDRS.encode(encoding_format) + response
    except FileNotFoundError:
        return (HDRS_404 + '404 Not Found.').encode(encoding_format)


# http://127.0.0.1:1500/home.html
# http://127.0.0.1:1500/friends.html
# http://127.0.0.1:1500/news.html

if __name__ == '__main__':
    start_server()
