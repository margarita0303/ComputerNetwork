import pygame
import socket 

def pygame_start(name):
    pygame.init()
    size = (350, 350)
    window = pygame.display.set_mode(size)
    window.fill((255, 255, 255))
    pygame.display.set_caption(name)
    pygame.display.update()
    return window

def start_server(host, port):
    is_active = True
    window = pygame_start('Server')
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    while is_active:
        request = server_socket.recvfrom(1024)[0].decode('utf-8').split()
        if request[0] == 'quit':
            is_active = False
        elif request[0] == 'point':
            x, y = int(request[1]), int(request[2])
            pygame.draw.circle(window, (0, 0, 0), (x, y), 3)
        elif request[0] == 'line':
            x1, y1, x2, y2 = int(request[1]), int(request[2]), int(request[3]), int(request[4])
            pygame.draw.line(window, (0, 0, 0), (x1, y1), (x2, y2), 3)
        pygame.display.update()
    pygame.quit()
    server_socket.close()


if __name__ == '__main__':
    host = input("Input host name: ")
    port = input("Input port: ")
    start_server(host, int(port))

