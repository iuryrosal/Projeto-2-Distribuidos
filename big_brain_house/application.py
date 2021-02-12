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
    time.sleep(2)
    client_socket.send(message)

# conecta via tcp com o servidor
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.bind(ADDR_APP)
client_socket.connect(GATEWAY_ADDR)
print("### conectado com o servidor")

# cria e serializa a mensagem a ser enviada
identification_message = messages_pb2.IdentificatioApplication()
identification_message.type = 'Application'
serialized_message = identification_message.SerializeToString()
print("### Serializando Mensagem")

# envio da mensagem
write(client_socket, serialized_message)
print("### Mensagem enviada")

# início da thread para fica escutando o server
receive_thread = threading.Thread(target=receive, args=(client_socket,  ))
receive_thread.start()




# write_thread = threading.Thread(target=write, args=(client_socket))
# write_thread.start()


# listar aparelhos disponiveis, ligar atributos dos aparelhos espeficos