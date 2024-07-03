import socket   # Import socket library for network communication
import threading   # Import threading library for running concurrent operations

# Constants
HOST = '127.0.0.1'   # Localhost IP address
PORT = 12345   # Port number for the server connection
ADDR = (HOST, PORT)   # Tuple containing the server address
FORMAT = 'utf-8'   # Encoding format for message encoding and decoding

# Initialize server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Create a new socket object
server.bind(ADDR)   # Bind the server socket to the address
server.listen()   # Start listening for incoming connections

clients = []   # List to store connected clients' sockets
nicknames = []   # List to store nicknames associated with each client

def broadcast(message):
    for client in clients:
        client.send(message)   # Send the message to all connected clients

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)   # Receive message from client
            broadcast(message)   # Broadcast the message to all clients
        except:
            index = clients.index(client)   # Get the index of the client
            clients.remove(client)   # Remove the client from the list
            client.close()   # Close the client socket
            nickname = nicknames[index]   # Get the nickname of the client
            broadcast(f'{nickname} left the chat!'.encode(FORMAT))   # Broadcast that the client left
            nicknames.remove(nickname)   # Remove the nickname from the list
            break   # Exit the loop

def receive():
    while True:
        client, address = server.accept()   # Accept a new client connection
        print(f"Connected with {str(address)}")   # Print client's address

        client.send('NICK'.encode(FORMAT))   # Send 'NICK' prompt to client
        nickname = client.recv(1024).decode(FORMAT)   # Receive and decode nickname from client
        nicknames.append(nickname)   # Add nickname to list
        clients.append(client)   # Add client socket to list

        print(f"Nickname of the client is {nickname}")   # Print client's nickname
        broadcast(f"{nickname} joined the chat!".encode(FORMAT))   # Broadcast that client joined
        client.send("Connected to the server!".encode(FORMAT))   # Confirm client connection

        thread = threading.Thread(target=handle_client, args=(client,))   # Create a thread for client handling
        thread.start()   # Start the thread

print("Server is listening...")   # Print message indicating server is listening
receive()   # Start receiving incoming connections
