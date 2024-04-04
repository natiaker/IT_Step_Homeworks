import socket

# create TCP socket for client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Client socket created")

# specify the server's IP address and port to connect to
SERVER_IP = '127.0.0.1'
SERVER_PORT = 8000

# connect the client socket to the server
client_socket.connect((SERVER_IP, SERVER_PORT))

# receive data from the server
received_message = client_socket.recv(1024).decode()
print(received_message)
client_socket.close()  # close the connection

