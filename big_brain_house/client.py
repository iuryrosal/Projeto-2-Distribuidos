import socket
import threading
import time

from multicast.receive_multicast_group import receive_multicast

class Client:
    FORMAT = "utf-8"
    
    def get_addr_by_mult(self):
        addr = receive_multicast().decode(Client.FORMAT)
        # Tratando o fortmato da mensagem
        addr = addr.split()
        addr[1] = int(addr[1])
        addr = tuple(addr)

        return addr

    def receive(self, client_socket):
        while True:
            try:
                message = client_socket.recv(1024).decode(Client.FORMAT)
                print(message)
            except:
                print("An error occured!")
                client_socket.close()
                break

    def write(self, client_socket, msg):
        client_socket.send(msg.encode(Client.FORMAT))

    def connect_tcp(self, addr):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(addr)
        client_socket.connect(addr)
        print("Conectado ao servidor!")

        receive_thread = threading.Thread(target = self.receive, args=(client_socket,))
        receive_thread.start()

        return client_socket

    #write_thread = threading.Thread(target = write, args=(client_socket, msg))
    #write_thread.start()

    # addr = get_addr_by_mult()
    # socket = connect_tcp(addr)
    # msg = 'Oi'
    # write(socket, msg)
    # receive(socket)