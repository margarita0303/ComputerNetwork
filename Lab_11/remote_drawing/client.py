import pygame
import socket 

def pygame_init(name):
    pygame.init()
    size = (350, 350)
    window = pygame.display.set_mode(size)
    window.fill((255, 255, 255))
    pygame.display.set_caption(name)
    pygame.display.update()
    return window

def start_client(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    window = pygame_init('Client')
    is_running = True
    is_pressed_mouse = False
    last_point = None

    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                client_socket.sendto('quit'.encode('utf-8'), (host, port))
            elif event.type == pygame.MOUSEBUTTONDOWN or (event.type == pygame.MOUSEMOTION and is_pressed_mouse):
                is_pressed_mouse = True
                x, y = pygame.mouse.get_pos()
                if last_point is None:
                    pygame.draw.circle(window, (0, 0, 0), (x, y), 3)
                    client_socket.sendto(f'point {x} {y}'.encode('utf-8'), (host, port))
                else:
                    x1, y1, x2, y2 = last_point[0], last_point[1], x, y
                    pygame.draw.line(window, (0, 0, 0), (x1, y1), (x2, y2), 3)
                    client_socket.sendto(f'line {last_point[0]} {last_point[1]} {x} {y}'.encode('utf-8'), (host, port))
                last_point = (x, y)
            elif event.type == pygame.MOUSEBUTTONUP:
                is_pressed_mouse = False
                last_point = None
        pygame.display.update()

    pygame.quit()
    client_socket.close()


if __name__ == '__main__':
    host = input("Input host name: ")
    port = input("Input port: ")
    start_client(host, int(port)) 
