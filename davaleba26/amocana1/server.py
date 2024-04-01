import socket

# create TCP socket for server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Server socket created")

# specify host and port to bind the socket to
HOST = '0.0.0.0'  # can receive requests from any host
PORT = 8000

server_socket.bind((HOST, PORT))

# listen to incoming connections
server_socket.listen()
print("Socket is now listening")

# wait for a connection
while True:
    # accept connection
    conn, addr = server_socket.accept()
    print("Connected by", addr)

    # send message to the client
    message = "Server -> Successfully connected"
    conn.sendall(message.encode())
    conn.close()  # close the connection
