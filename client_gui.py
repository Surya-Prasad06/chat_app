import socket   # Import socket library for network communication
import threading   # Import threading library for running concurrent operations
import tkinter as tk   # Import tkinter for GUI elements
from tkinter import scrolledtext, messagebox, simpledialog   # Import specific tkinter components

# Constants
HOST = '127.0.0.1'   # Localhost IP address
PORT = 12345   # Port number for the server connection
ADDR = (HOST, PORT)   # Tuple containing the server address
FORMAT = 'utf-8'   # Encoding format for message encoding and decoding

# Initialize client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Create a new socket object
try:
    client.connect(ADDR)   # Attempt to connect to the server
except ConnectionRefusedError as e:   # Handle connection errors
    messagebox.showerror("Connection Error", f"Could not connect to the server: {e}")   # Show error message
    exit()   # Exit the application if connection fails

class ChatApp:
    def __init__(self, master):
        self.master = master   # Main window (root)
        self.master.title("Chat Application")   # Set window title

        self.chat_label = tk.Label(master, text="Chat:")   # Create a label for the chat area
        self.chat_label.pack(padx=20, pady=5)   # Pack the label with padding

        self.text_area = scrolledtext.ScrolledText(master)   # Create a scrolled text area for chat messages
        self.text_area.pack(padx=20, pady=5)   # Pack the text area with padding
        self.text_area.config(state='disabled')   # Disable editing of the text area

        self.msg_label = tk.Label(master, text="Message:")   # Create a label for the message entry
        self.msg_label.pack(padx=20, pady=5)   # Pack the label with padding

        self.msg_entry = tk.Entry(master, width=50)   # Create an entry widget for typing messages
        self.msg_entry.pack(padx=20, pady=5)   # Pack the entry with padding
        self.msg_entry.bind("<Return>", self.write_message)   # Bind the Enter key to send messages

        self.send_button = tk.Button(master, text="Send", command=self.write_message)   # Create a send button
        self.send_button.pack(padx=20, pady=5)   # Pack the button with padding

        self.nickname = self.get_nickname()   # Prompt for and get the user's nickname
        if not self.nickname:   # Exit if no nickname is provided
            exit()

        self.receive_thread = threading.Thread(target=self.receive_messages)   # Create a thread for receiving messages
        self.receive_thread.start()   # Start the thread

    def get_nickname(self):
        nickname = simpledialog.askstring("Nickname", "Choose your nickname")   # Prompt for a nickname
        if nickname:
            client.send(nickname.encode(FORMAT))   # Send the nickname to the server
            return nickname   # Return the nickname
        else:
            return None   # Return None if no nickname is provided

    def receive_messages(self):
        while True:
            try:
                message = client.recv(1024).decode(FORMAT)   # Receive messages from the server
                self.text_area.config(state='normal')   # Enable editing to insert new message
                self.text_area.insert(tk.END, message + '\n')   # Insert the received message
                self.text_area.config(state='disabled')   # Disable editing after inserting message
                self.text_area.yview(tk.END)   # Scroll to the end of the text area
            except:   # Handle exceptions (e.g., server disconnection)
                client.close()   # Close the client socket
                break   # Exit the loop

    def write_message(self, event=None):
        message = f'{self.nickname}: {self.msg_entry.get()}'   # Format the message with the nickname
        client.send(message.encode(FORMAT))   # Send the message to the server
        self.msg_entry.delete(0, tk.END)   # Clear the entry widget

root = tk.Tk()   # Create the main window (root)
app = ChatApp(root)   # Instantiate the ChatApp class with the main window
root.mainloop()   # Start the Tkinter event loop
