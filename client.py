import socket   # Import socket library for network communication
import threading   # Import threading library for running concurrent operations

# Constants
HOST = '127.0.0.1'   # Localhost IP address
PORT = 12345   # Port number for the server connection
ADDR = (HOST, PORT)   # Tuple containing the server address
FORMAT = 'utf-8'   # Encoding format for message encoding and decoding

# Initialize client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Create a new socket object
client.connect(ADDR)   # Connect to the server using the address

nickname = input("Choose your nickname: ")   # Prompt the user to choose a nickname

def receive():
    while True:
        try:
            message = client.recv(1024).decode(FORMAT)   # Receive messages from the server
            if message == 'NICK':
                client.send(nickname.encode(FORMAT))   # Send the chosen nickname to the server
            else:
                print(message)   # Print the received message
        except:
            print("An error occurred!")   # Handle errors
            client.close()   # Close the client socket
            break   # Exit the loop

def write():
    while True:
        message = f'{nickname}: {input("")}'   # Construct the message with the nickname
        client.send(message.encode(FORMAT))   # Send the message to the server

receive_thread = threading.Thread(target=receive)   # Create a thread for receiving messages
receive_thread.start()   # Start the receiving thread

write_thread = threading.Thread(target=write)   # Create a thread for writing messages
write_thread.start()   # Start the writing thread
