import socket
import threading
import generated.messages_pb2 as messages_pb2
import time

GATEWAY_IP = socket.gethostbyname(socket.gethostname())
GATEWAY_PORT = 37020
GATEWAY_ADDR = (GATEWAY_IP, GATEWAY_PORT)
FORMAT = 'utf-8'

IP_APP = socket.gethostbyname(socket.gethostname())
PORT_APP = 5555
ADDR_APP = (IP_APP, PORT_APP)

def receive(client_socket):
    while True:
      try:
          message = client_socket.recv(1024).decode(FORMAT)
          print(message)
      except:
          print("An error occured!")
          client_socket.close()
          break

def write(client_socket, message):
    print("### Enviando mensagem")
    client_socket.send(message)

def list_objects(client_socket):
    identification_message = messages_pb2.ApplicationMessage()
    identification_message.type = messages_pb2.ApplicationMessage.MessageType.COMMAND
    identification_message.command = "list_objects"

    print("### Serializando Mensagem")
    serialized_message = identification_message.SerializeToString()

    write(client_socket, serialized_message)
    print("### Mensagem enviada")

# conecta via tcp com o servidor
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.bind(ADDR_APP)
client_socket.connect(GATEWAY_ADDR)
print("### conectado com o servidor")

# início da thread para fica escutando o server
receive_thread = threading.Thread(target=receive, args=(client_socket,  ))
receive_thread.start()
print("### Escutando respostas do servidor")

list_objects(client_socket)
