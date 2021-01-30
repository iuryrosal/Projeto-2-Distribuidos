import socket
import threading

FORMAT = 'utf-8'
connected = 0

def receive(client_socket, nickname):
    global connected
    while True:
        try:
            message = client_socket.recv(1024).decode('ascii')
            if message == 'NICK':
                client_socket.send(nickname.encode('ascii'))
            elif message == 'Desconectado com sucesso!':
                print(message)
                connected = 0
                write_thread.join()
                receive_thread.join()
                client_socket.close()
                break
            else:
                print(message)
        except:
            print("An error occured!")
            client_socket.close()
            break

def write(client_socket, nickname):
    global connected
    while True:
        if connected == 1:
            text = input('')
            if text[0] == '/':
                client_socket.send(text.encode(FORMAT))
            else:
                message = '{}: {}'.format(nickname, text)
                client_socket.send(message.encode(FORMAT))

if connected == 0:
    input_i = input('')
    if input_i == '/ENTRAR':
        print("Para realizar a conexão, solicitamos o IP, porta do servidor e o nickname.")
        server = input("IP do Servidor: ")
        port = input("Porta do Servidor: ")
        nickname = input("Choose your nickname: ")

        ADDR = (server, int(port))

        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(ADDR)
            print("Servidor Conectado!")

            connected = 1
            receive_thread = threading.Thread(target=receive, args=(client_socket, nickname))
            receive_thread.start()

            write_thread = threading.Thread(target=write, args=(client_socket, nickname))
            write_thread.start()

        except Exception as e:
            print(e)