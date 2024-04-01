#  client.py
import socket
import threading


SERVER_IP = '127.0.0.1'
SERVER_PORT = 45678

nickname = input("Enter your nickname: ")

client_socket = socket.socket()
client_socket.connect((SERVER_IP, SERVER_PORT))


def receive_message():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message == "Nickname":
                client_socket.send(nickname.encode())
            else:
                print(message)
        except:
            print("Error!!!")
            client_socket.close()
            break


def write_message():
    while True:
        message = f"{nickname} -> {input()}"
        client_socket.send(message.encode())
        with open("messages.txt", "a") as file:
            file.write(message + "\n")


receive_thread = threading.Thread(target=receive_message)
receive_thread.start()
write_thread = threading.Thread(target=write_message)
write_thread.start()


