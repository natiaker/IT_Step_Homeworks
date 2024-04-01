#  server.py
import socket
import threading


HOST = '127.0.0.1'
PORT = 45678

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Server Socket Created!!!")

server_socket.bind((HOST, PORT))
server_socket.listen()
print(f"Server Socket Listening {PORT}")

clients = []
nicknames = []


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client_socket)
            clients.remove(client_socket)
            client_socket.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            break


def receive():
    while True:
        client, address = server_socket.accept()
        print(f"Connected with {address}")

        client.send("Nickname".encode())
        nickname = client.recv(1024).decode()

        nicknames.append(nickname)
        clients.append(client)

        print(f"{nickname} connected")
        broadcast(f"{nickname} joined the chat".encode())

        thread = threading.Thread(target=handle, args=(client, ))
        thread.start()


receive()
