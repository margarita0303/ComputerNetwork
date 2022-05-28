import os

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def run_server(HOST, PORT):
    authorizer = DummyAuthorizer()
    authorizer.add_user('test_user', '123456', '.')

    handler = FTPHandler
    handler.authorizer = authorizer
    handler.banner = "pyftpdlib based ftpd ready."

    address = (HOST, PORT)
    server = FTPServer(address, handler)
    
    server.max_cons = 256
    server.max_cons_per_ip = 5

    server.serve_forever()
    

if __name__ == '__main__':
    print("Input HOST:")
    HOST = input()
    print("Input PORT:")
    PORT = input()
    run_server(HOST, int(PORT)) 

