import socket
import threading
import sqlite3

HOST = '127.0.0.1' 
PORT = 12345 
CHATROOM_PASSWORD = 'password123'  
ADMIN_USERNAME = 'admin'  

conn = sqlite3.connect('chatroom.db', check_same_thread=False)
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        ip TEXT,
        message TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')
conn.commit()

clients = []
usernames = set() 

user_message_count = {}

def handle_client(client_socket, addr):
    print(f"Connection from {addr} has been established!")
    
    client_socket.send("Enter your name: ".encode())
    
    while True:
        name = client_socket.recv(1024).decode()
        if name and name not in usernames:
            usernames.add(name)
            user_message_count[name] = {'last_message': None, 'count': 0}  
            break
        else:
            client_socket.send("Username already taken or invalid. Please choose another name: ".encode())

    client_socket.send("Enter chatroom password: ".encode())
    password = client_socket.recv(1024).decode()

    if password != CHATROOM_PASSWORD:
        client_socket.send("Incorrect password. Disconnecting...".encode())
        client_socket.close()
        return

    clients.append((client_socket, addr, name))
    welcome_msg = f"{name} has joined the chat!"
    broadcast(welcome_msg.encode())

    while True:
        try:
            msg = client_socket.recv(1024).decode()
            if msg:
                if len(msg) > 100:
                    client_socket.send("Message exceeds 100 characters. Please try again.".encode())
                    continue

                if user_message_count[name]['last_message'] == msg:
                    user_message_count[name]['count'] += 1
                    if user_message_count[name]['count'] >= 5:
                        client_socket.send("You have been kicked for sending the same message too many times.".encode())
                        broadcast(f"{name} has been kicked for spamming.".encode())
                        client_socket.close()
                        clients.remove((client_socket, addr, name))
                        usernames.remove(name)
                        return
                else:
                    user_message_count[name] = {'last_message': msg, 'count': 1}  

                formatted_msg = f"{name} ({addr[0]}): {msg}"
                broadcast(formatted_msg.encode())
                c.execute("INSERT INTO messages (username, ip, message) VALUES (?, ?, ?)",
                          (name, addr[0], msg))
                conn.commit()
            else:
                break
        except Exception as e:
            print(f"Error: {e}")
            break

    client_socket.close()
    clients.remove((client_socket, addr, name))
    usernames.remove(name)
    broadcast(f"{name} has left the chat.".encode())

def broadcast(message):
    for client_socket, _, _ in clients:
        try:
            client_socket.send(message)
        except Exception as e:
            print(f"Error sending message to a client: {e}")
            client_socket.close()

def handle_kick(command, admin_name):
    _, username_to_kick = command.split(" ", 1)
    if username_to_kick in usernames:
        for client_socket, addr, name in clients:
            if name == username_to_kick:
                client_socket.send("You have been kicked from the chat.".encode())
                client_socket.close()
                clients.remove((client_socket, addr, name))
                usernames.remove(username_to_kick)
                broadcast(f"{username_to_kick} has been kicked from the chat by {admin_name}.".encode())
                return
    else:
        print(f"User {username_to_kick} not found.")

def show_messages():
    while True:
        command = input("Enter command (type 'exit' to quit): ")
        if command.lower() == 'show messages':
            c.execute("SELECT username, ip, message, timestamp FROM messages")
            messages = c.fetchall()
            if messages:
                print("\nStored messages:")
                for message in messages:
                    print(f"[{message[3]}] {message[0]} ({message[1]}): {message[2]}")
            else:
                print("No messages stored.")
        elif command.lower() == 'exit':
            break

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Server started on {HOST}:{PORT}")

    thread = threading.Thread(target=show_messages)
    thread.daemon = True  
    thread.start()

    while True:
        client_socket, addr = server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        thread.start()

if __name__ == "__main__":
    start_server()
