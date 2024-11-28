import socket
import threading
import re

HOST = '127.0.0.1'
PORT = 12345

def is_valid_name(name):
    return bool(re.match("^[A-Za-z0-9_]+$", name))

def receive_messages(client_socket):
    while True:
        try:
            msg = client_socket.recv(1024).decode()
            if msg:
                print("\n" + msg)
            else:
                break
        except Exception as e:
            print(f"An error occurred: {e}")
            client_socket.close()
            break

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    while True:
        name = input("Enter your name: ")
        if not is_valid_name(name):
            print("Invalid name. Only alphanumeric characters and underscores are allowed.")
            continue
        client_socket.send(name.encode())

        response = client_socket.recv(1024).decode()
        if "already taken" in response:
            print(response)
        else:
            print(response)
            break

    while True:
        password = input("Enter chatroom password: ")
        client_socket.send(password.encode())

        response = client_socket.recv(1024).decode()
        if "Disconnecting" in response:
            print(response)
            client_socket.close()
            return
        else:
            print("Password accepted.")
            break

    thread = threading.Thread(target=receive_messages, args=(client_socket,))
    thread.start()

    while True:
        msg = input()
        if msg.lower() == 'exit':
            break
        try:
            client_socket.send(msg.encode())
        except Exception as e:
            print(f"Error sending message: {e}")
            break

    client_socket.close()

if __name__ == "__main__":
    main()
