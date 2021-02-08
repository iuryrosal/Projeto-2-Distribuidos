import socket
import threading

class Communication:
    def __init__(self, type, server, port):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(ADDR)
        print("Servidor Conectado!")


