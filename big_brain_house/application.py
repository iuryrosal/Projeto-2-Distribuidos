import socket
import threading

GATEWAY_IP = socket.gethostbyname(socket.gethostname())
GATEWAY_PORT = 37020
ADDR = (GATEWAY_IP, GATEWAY_PORT)
FORMAT = 'utf-8'

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
    client_socket.send(message.encode(FORMAT))

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(ADDR)
write(client_socket, "Application")

receive_thread = threading.Thread(target=receive, args=(client_socket,  ))
receive_thread.start()

write(client_socket, "######Teste########")


# write_thread = threading.Thread(target=write, args=(client_socket))
# write_thread.start()

