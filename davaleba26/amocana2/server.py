import socket
import threading

# define server's IP address and port number
HOST = '127.0.0.1'  # localhost
PORT = 45678  

# create server socket using ipv4 amd TCP protocol
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Server Socket Created!!!")


# bind the server to the specific address and port and start listening for incoming connections
server_socket.bind((HOST, PORT))
server_socket.listen()
print(f"Server Socket Listening {PORT}")


clients = []
nicknames = []


# function which sends messages to all connected clients
def broadcast(message):
    for client in clients:
        client.send(message)


# function to handle communication with a client
def handle(client_socket):
    while True:
        try:
            # receive message from the client and broadcast to all clients
            message = client_socket.recv(1024)
            broadcast(message)
        except:
            # in case of error will be executed this code: will be removed that client and nickname from the list
            index = clients.index(client_socket)
            clients.remove(client_socket)
            client_socket.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            break


# accept and handle incoming connections
def receive():
    while True:
        client, address = server_socket.accept()
        print(f"Connected with {address}")

        # request client to send its nickname
        client.send("Nickname".encode())
        nickname = client.recv(1024).decode()  # receive and decode nickname sent from the client

        # add nickname and client to the lists
        nicknames.append(nickname)
        clients.append(client)

        print(f"{nickname} connected")
        broadcast(f"{nickname} joined the chat".encode())

        # create new thread to handle communication with the client
        thread = threading.Thread(target=handle, args=(client, ))
        thread.start()


receive()
