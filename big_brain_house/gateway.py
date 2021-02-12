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

application_address = None


def start_server():
    server_tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_tcp_socket.bind(ADDR)
    server_tcp_socket.listen()
    print("Servidor ligado!\n")
    return server_tcp_socket

def send_gateway_address():
    message = f"{IP} {PORT}"
    send_multicast(message)

def handle(client):
    while True:
        message = client.recv(1024)
        message_decoded = message.decode(FORMAT)
        print(message_decoded)
        answer = 'Retorno do gateway: Você esta conectado via TCP\n'
        client.send(answer.encode(FORMAT))

def application_handle(client):
    print("Conectado a applicação via TCP\n")

    while True:
        message = client.recv(1024)
        message_decoded = message.decode(FORMAT)
        print(message_decoded)
        answer = 'Retorno do gateway: Você esta conectado via TCP\n'
        client.send(answer.encode(FORMAT))


def connect_client_by_tcp(server_tcp_socket):
    print("Aguardando conexões TCP...\n")
    
    while True:
        client, address = server_tcp_socket.accept()
        client_type = client.recv(1024).decode(FORMAT)

        if client_type != 'Application':
            clients_types.append(client_type)
            clients.append(client)
            print(f"Clientes conectados:{clients},\n Tipos:{clients_types}\n\n")
            
            print("Connected with {}\n".format(str(address)))

            thread = threading.Thread(target=handle, args=(client,))
            thread.start()

            # teste para mudança de status dos objetos
            time.sleep(2)
            msg = "status True"
            send_command(0,msg)
        else:
            application_address = client
            application_thread = threading.Thread(target=application_handle, args=(client,))
            application_thread.start()


def send_command(client_index, message):
    clients[client_index].send(message.encode(FORMAT))

 

server_tcp_socket = start_server()
send_gateway_address()
connect_client_by_tcp(server_tcp_socket)









