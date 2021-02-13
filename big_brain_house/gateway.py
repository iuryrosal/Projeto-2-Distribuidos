import socket
import time
import threading
import generated.messages_pb2 as messages_pb2

from multicast.send_multicast_group import send_multicast 

IP = socket.gethostbyname(socket.gethostname())
PORT = 37020
ADDR = (IP, PORT)
FORMAT = "utf-8"

ADDR_APP = ('127.0.1.1', 5555)

clients_types = [] 
clients = []


def start_server():
    server_tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_tcp_socket.bind(ADDR)
    server_tcp_socket.listen()
    print("Servidor ligado!\n")
    return server_tcp_socket

def send_gateway_address():
    message = f"{IP} {PORT}"
    send_multicast(message)

def send_command_to_object(client_index, message):
    clients[client_index].send(message.encode(FORMAT))

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            message_decoded = message.decode(FORMAT)

            answer = 'Retorno do gateway: Você esta conectado via TCP\n'
            client.send(answer.encode(FORMAT))
        except:
            print("An error occured!")
            client.close()
            break

def return_list_object(client):
    answer = messages_pb2.GatewayMessage()
    answer.response_type = messages_pb2.GatewayMessage.MessageType.LIST
    
    for o in clients_types:
        iobject = answer.object.add()
        iobject.type = o

    answer_serialized = answer.SerializeToString()

    client.send(answer_serialized)

def return_object_status(client, consulted_object):
    answer = messages_pb2.GatewayMessage()
    answer.response_type = messages_pb2.GatewayMessage.MessageType.GET

    for o in clients_types:
        if o == consulted_object:
            iobject = answer.object.add()
            iobject.type = o 

            answer_serialized = answer.SerializeToString()
            client.send(answer_serialized)

def set_object_status(client, args):
    iobject, new_status = args.split()[0], args.split()[1]

    for i in range(0, len(clients_types)):
        if clients_types[i] == iobject:
            send_command_to_object(i , f"status {new_status}")

def application_handle(client):
    while True:
        try:
            print("Recebendo mensagens da apliação")
            message = client.recv(1024)
            message_decoded = messages_pb2.ApplicationMessage()
            message_decoded.ParseFromString(message)
            
            if message_decoded.type == 1:
                if message_decoded.command == 'list_objects':
                    return_list_object(client)
                if message_decoded.command == 'get_status':
                    return_object_status(client, message_decoded.args)
                if message_decoded.command == 'set_status':
                    set_object_status(client, message_decoded.args)
        except:
            print("An error occured!")
            client_socket.close()
            break
                    
def connect_client_by_tcp(server_tcp_socket):
    print("Aguardando conexões TCP...\n")
    
    while True:
        try:
            client, address = server_tcp_socket.accept()

            # encaminhamento para a thread que irá lidar com as requisições da applicação ou para a thread dos objetos
            if address == ADDR_APP: 
                application_thread = threading.Thread(target=application_handle, args=(client,))
                application_thread.start()
            else:
                # registra os clientes antes de iniciar a thread
                client_type = client.recv(1024).decode(FORMAT)
                clients_types.append(client_type)
                clients.append(client)
            
                print("Connected with {}\n".format(str(address)))

                thread = threading.Thread(target=handle, args=(client,))
                thread.start()
        except Exception as e:
            print(e)

server_tcp_socket = start_server()
send_gateway_address()
connect_client_by_tcp(server_tcp_socket)
