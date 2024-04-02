import socket
import threading

# define server IP address and port number
SERVER_IP = '127.0.0.1'
SERVER_PORT = 45678

# get user's nickname
nickname = input("Enter your nickname: ")

# create client's socket
client_socket = socket.socket()
# connect to the server using the defined IP address and port
client_socket.connect((SERVER_IP, SERVER_PORT))


# function to receive messages from the server.
def receive_message():
    while True:
        try:
            # recieve message from server and decode it
            message = client_socket.recv(1024).decode()
            # if message is a request for nickname, send the nickname to the srver, in other case print received message
            if message == "Nickname":
                client_socket.send(nickname.encode())
            else:
                print(message)
        except:
            # handle exceptions by printing an error message and close the client socket
            print("Error!!!")
            client_socket.close()
            break

# function to write and send messages to the server
def write_message():
    while True:
        # get user inpt for the message and send to the server
        message = f"{nickname} -> {input()}"
        client_socket.send(message.encode())

        # save/append message to a text file
        with open("messages.txt", "a") as file:
            file.write(message + "\n")


# create a thread to receive messages concurently 
receive_thread = threading.Thread(target=receive_message)
receive_thread.start()
# create thread to write messages concurrently
write_thread = threading.Thread(target=write_message)
write_thread.start()


