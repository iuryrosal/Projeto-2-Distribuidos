import socket
import threading
import time

FORMAT = "utf-8"

def get_addr_by_broad():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) # UDP

    client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    client.bind(("", 37020))
    while True:
        data, addr = client.recvfrom(1024)
        data = data.decode(FORMAT)
        data = data.split()
        data[1] = int(data[1])
        data = tuple(data)
        if data != None:
            break
    return data

def receive(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('ascii')
            print(message)
        except:
            print("An error occured!")
            client_socket.close()
            break

def write(client_socket, msg):
    #while True:
    text = msg + '\n'
    client_socket.send(text.encode(FORMAT))
    time.sleep(2)


def connect_tcp(addr):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(addr)
    client_socket.connect(addr)
    print("Servidor Conectado!")

    return client_socket

#receive_thread = threading.Thread(target = receive, args=(client_socket,))
#receive_thread.start()

#write_thread = threading.Thread(target = write, args=(client_socket, msg))
#write_thread.start()

addr = get_addr_by_broad()
socket = connect_tcp(addr)
msg = 'Oi'
write(socket, msg)
receive(socket)