# TODO
# create a simple server that accepts connects
import socket
import selectors
import sys
import types

sel = selectors.DefaultSelector()


HOST = "" # sys.argv[1] or "127.0.0.1"
PORT = 9000

def accept_wrapper(sock):
    conn, addr = sock.accept()
    print(f"Accepted conneciton from: {addr}")
    conn.setblocking(False)

    data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")

    events = selectors.EVENT_READ | selectors.EVENT_WRITE

    sel.register(conn, events, data=data)

def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)  # Should be ready to read
        if recv_data:
            data.outb += recv_data
        else:
            print(f"Closing connection to {data.addr}")
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print(f"Echoing {data.outb!r} to {data.addr}")
            sent = sock.send(data.outb)  # Should be ready to write
            data.outb = data.outb[sent:]


# with socket.socket(
#     socket.AF_INET , # socket famliy (IPv4)
#     socket.SOCK_STREAM # socket type TCP
# ) as s:
#     s.bind(
#         (
#             HOST, # hostname/ipv4/v6 or blank to accept all IPv4/v6 
#             PORT
#         )
#     )
#     s.listen() # enables the server to accept connection

#     conn, addr = s.accept() # waits for connection from the client

#     with conn:
#         print(f"Connection addr {addr}")
#         while True:
#             data = conn.recv(1024)
#             if not data:
#                 print("No data")
#                 break
#             conn.sendall(data)
            
lsock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

lsock.bind((HOST, PORT))

lsock.listen()
print(f"Listening on Port: {PORT}")

lsock.setblocking(False)
sel.register(lsock, selectors.EVENT_READ, data=None)

try:
    while True:
        events = sel.select(timeout=None)
        for key, mask in events:
            if key.data is None:
                accept_wrapper(key.fileobj)
            else:
                service_connection(key, mask)

except KeyboardInterrupt:
    print("Server is closed")
finally:   
    sel.close()