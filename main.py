# TODO
# bind ip add to server
# ip address stored in file (clients.json)
# connect to server
# collect message
# receive messages
import socket


HOST = "127.0.0.1"
PORT = 9000
HOSTNAME = socket.gethostname()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    conn  = s.connect((HOST,PORT))
    while True:
        try:
            msg = input(f"{HOSTNAME}>> ")
            s.sendall(msg.encode())
            data = s.recv(1024)
            print(f"Received data: {data.decode()}")
        except socket.error:
            break
        except KeyboardInterrupt:
            print("Connection closed")
            break
