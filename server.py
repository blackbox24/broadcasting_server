# TODO
# create a simple server that accepts connects
import socket

HOST = "127.0.0.1"
PORT = 9000

with socket.socket(
    socket.AF_INET , # socket famliy (IPv4)
    socket.SOCK_STREAM # socket type TCP
) as s:
    s.bind(
        (
            HOST, # hostname/ipv4/v6 or blank to accept all IPv4/v6 
            PORT
        )
    )
    s.listen() # enables the server to accept connection

    conn, addr = s.accept() # waits for connection from the client

    with conn:
        print(f"Connection addr {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                print("No data")
                break
            conn.sendall(data)
            
