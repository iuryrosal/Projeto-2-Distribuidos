import socket
import time
import threading

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

def scan_broad():
    server_broadcast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

    server_broadcast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    server_broadcast_socket.settimeout(0.2)
    message = f"{IP} {PORT}".encode(FORMAT)
    for i in range(5):
        server_broadcast_socket.sendto(message, ('<broadcast>', 0))
        print("Message Sent!")
        time.sleep(1)

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
scan_broad()
connect_client_by_tcp(server_tcp_socket)