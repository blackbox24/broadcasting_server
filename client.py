import socket 
import threading


HOST, PORT = "127.0.0.1", 5000
hostname = socket.gethostname()

def receive_msg(sock):
    while True:
        try:
            print(f"Msg: {sock.recv(1024).decode()}")
        except:
            break

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
threading.Thread(target=receive_msg, args=(sock,), daemon=True).start()

while True:
    try:
        
        msg = input(f"{hostname}> ")
        sock.send(msg.encode())
    except:
        print("You closed connection")
        sock.close()
        exit()