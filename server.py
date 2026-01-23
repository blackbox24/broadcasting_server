from utils.helpers import read_file, write_file
import socket
import threading
import logging
import json
import os


logging.basicConfig(level=logging.INFO, format="%(message)s")  # type: ignore
logger = logging.getLogger(__name__)

HOST, PORT = "127.0.0.1", 5000
clients = []  # Keep track of connected clients for broadcasting
users = []
file = "clients.json"


# Ensure chat file exists
if not os.path.isfile(file):
    with open(file, "w") as f:
        json.dump([{"users": []}], f)
        
def broadcast_msg(data, client_sock):
    for client in clients:
        if client != client_sock:
            client.send(data.encode())
            logger.info("Message sent")


def handle_connection(client):
    while True:
        try:
            data = client.recv(1024).decode()
            if not data:
                break
            write_file(file,users)
            broadcast_msg(data, client)
        except:
            clients.remove(client)
            users.remove(f"{client.getpeername()[0]}:{client.getpeername()[1]}")
            write_file(file,users)
            client.close()
            break


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen()

print(f"Server running on {HOST}:{PORT}")
while True:
    try:
        client_sock, addr = sock.accept()
        logger.info(f"{addr} connected to server")
        clients.append(client_sock)
        users.append(f"{addr[0]}:{addr[1]}")
        threading.Thread(target=handle_connection, args=(client_sock,)).start()

    except KeyboardInterrupt:
        logger.info("connection interrapted")
        exit(0)
