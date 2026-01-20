# TODO
# create a simple server that accepts connects
# import socket
# import selectors
# import sys
# import types

# sel = selectors.DefaultSelector()


# HOST = "" # sys.argv[1] or "127.0.0.1"
# PORT = 9000

# def accept_wrapper(sock):
#     conn, addr = sock.accept()
#     print(f"Accepted conneciton from: {addr}")
#     conn.setblocking(False)

#     data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")

#     events = selectors.EVENT_READ | selectors.EVENT_WRITE

#     sel.register(conn, events, data=data)

# def service_connection(key, mask):
#     sock = key.fileobj
#     data = key.data
#     if mask & selectors.EVENT_READ:
#         recv_data = sock.recv(1024)  # Should be ready to read
#         if recv_data:
#             data.outb += recv_data
#         else:
#             print(f"Closing connection to {data.addr}")
#             sel.unregister(sock)
#             sock.close()
#     if mask & selectors.EVENT_WRITE:
#         if data.outb:
#             print(f"Echoing {data.outb!r} to {data.addr}")
#             sent = sock.send(data.outb)  # Should be ready to write
#             data.outb = data.outb[sent:]


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
            
# lsock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# lsock.bind((HOST, PORT))

# lsock.listen()
# print(f"Listening on Port: {PORT}")

# lsock.setblocking(False)
# sel.register(lsock, selectors.EVENT_READ, data=None)

# try:
#     while True:
#         events = sel.select(timeout=None)
#         for key, mask in events:
#             if key.data is None:
#                 accept_wrapper(key.fileobj)
#             else:
#                 service_connection(key, mask)

# except KeyboardInterrupt:
#     print("Server is closed")
# finally:   
#     sel.close()

import asyncio
import json
import websockets


async def echo_handler(websocket):
    # TODO:
    # Handle incoming websocket connection and echos messages back to client

    print(f"Client connected from : {websocket.remote_address}")
    try:
        async for message in websocket:
            print(f"Received message from client: {message}")
            response = f"Server Echo: {message}"
            await websocket.send(response)

            print(f"Sent message: {response}")
    except websockets.exceptions.ConnectionClosed as e:
        print(f"Connection closed: {e}")

    finally:
        print(f"Connection closed path: {websocket.remote_address}")

async def main():
    async with websockets.serve(echo_handler, "localhost",8765):
        print("Websocket server started and listening on we://localhost:8765")
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())