import socket
import time
import threading

from multicast.send_multicast_group import send_multicast 

PORT = 37020
IP = socket.gethostbyname(socket.gethostname())
ADDR = (IP, PORT)
FORMAT = "utf-8"

def start_server():
    server_tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_tcp_socket.bind(ADDR)
    server_tcp_socket.listen()
    print("Servidor ligado!")
    return server_tcp_socket

def send_gateway_address():
    message = f"{IP} {PORT}"
    send_multicast(message)

def handle(client):
    while True:
        message = client.recv(1024)
        message_decoded = message.decode(FORMAT)
        print(message_decoded)
        answer = 'Gostosa'
        client.send(answer.encode(FORMAT))

def connect_client_by_tcp(server_tcp_socket):
    print("Aguardando conexão...")
    while True:
        client, address = server_tcp_socket.accept()
        print("Connected with {}".format(str(address)))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

server_tcp_socket = start_server()
send_gateway_address()
connect_client_by_tcp(server_tcp_socket)