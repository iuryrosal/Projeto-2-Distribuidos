import socket
import time
import threading

from multicast.send_multicast_group import send_multicast 

PORT = 37020
IP = socket.gethostbyname(socket.gethostname())
ADDR = (IP, PORT)
FORMAT = "utf-8"
clients_types = [] 
clients = []


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
        answer = 'Você esta conectado via TCP'
        client.send(answer.encode(FORMAT))

def connect_client_by_tcp(server_tcp_socket):
    print("Aguardando conexões...")
    
    while True:
        client, address = server_tcp_socket.accept()
        client_type = client.recv(1024).decode(FORMAT)

        clients_types.append(client_type)
        clients.append(client)
        print(f"Clientes conectados:{clients},\n Tipos:{clients_types}\n\n")
        
        print("Connected with {}".format(str(address)))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

        # teste para mudança de status dos objetos
        time.sleep(2)
        msg = "status True"
        send_command(0,msg)



def send_command(client_index, message):
    clients[client_index].send(message.encode(FORMAT))

 



server_tcp_socket = start_server()
send_gateway_address()
connect_client_by_tcp(server_tcp_socket)









