Chat Application with GUI using Python

This project is a simple chat application built using Python. It includes both a server and a client with a graphical user interface (GUI) built using Tkinter. The application allows multiple clients to connect to the server and exchange messages in real time.

Project Structure:
==================
chat_app/
    ├── server.py       # The server code
    ├── client.py       # The command-line client code (optional)
    ├── client_gui.py   # The GUI client code
    └── README.txt      # This readme file

Requirements:
=============
- Python 3.x
- Tkinter (usually comes pre-installed with Python)

How to Run:
===========

1. Start the Server:
   -----------------
   Open a terminal or command prompt.
   Navigate to the directory where server.py is located.
   Run the server with the following command:

       python server.py

   The server will start and listen for incoming connections on 127.0.0.1:12345.

2. Start the Client with GUI:
   --------------------------
   Open another terminal or command prompt.
   Navigate to the directory where client_gui.py is located.
   Run the client with the following command:

       python client_gui.py

   A GUI window will appear prompting you to enter a nickname. Enter your desired nickname to join the chat.

3. Start Additional Clients:
   -------------------------
   To fully test the chat application, you can start multiple instances of the client.
   Open new terminals or command prompts and run client_gui.py again as described above.

   Each client will connect to the server and allow users to send and receive messages in real time.

File Descriptions:
==================

- server.py:
  This file contains the server code that listens for incoming client connections, handles message broadcasting, and manages connected clients.

- client.py:
  This is an optional command-line client for the chat application. It connects to the server and allows message exchange via the terminal.

- client_gui.py:
  This file contains the GUI client code built using Tkinter. It provides a user-friendly interface for chatting, including a text area for displaying messages, an entry field for typing messages, and a send button.

Common Issues and Troubleshooting:
==================================
- Ensure the server is running before starting any clients.
- Make sure the server and clients are using the same IP address (127.0.0.1) and port (12345).
- If you encounter a ConnectionRefusedError, verify that the server is running and listening on the correct port.
- Check for firewall or antivirus settings that might be blocking the connection.

Dependencies:
=============
This project uses the standard library modules in Python:
- socket
- threading
- tkinter

These modules are included with Python, so no additional installations are required.

Contact:
========
For any questions or issues, please contact [your contact information].

Enjoy chatting!
