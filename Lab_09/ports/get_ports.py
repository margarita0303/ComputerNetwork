import socket

if __name__ == '__main__':
    target = input('Enter host name: ')
    port_begin = int(input('Enter start number of ports: '))
    port_end = int(input('Enter end number of ports: '))
    try:
        print('Opened ports:')
        socket.setdefaulttimeout(0.1)
        for port in range(port_begin, port_end + 1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            res = s.connect_ex((target, port))
            if res == 0:
                print(port)
            s.close()
                
    except socket.gaierror:
        print('Can not get the server.')
    except socket.error:
        exit(1)
        print('Can not get the server.') 
        exit(1)
