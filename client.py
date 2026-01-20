# TODO
# bind ip add to server
# ip address stored in file (clients.json)
# connect to server
# collect message
# receive messages

# PART 1
# import socket
# import selectors
# import types
# import sys

# HOST = "127.0.0.1"
# PORT = 9000
# HOSTNAME = socket.gethostname()

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     conn  = s.connect((HOST,PORT))
#     while True:
#         try:
#             msg = input(f"{HOSTNAME}>> ")
#             s.sendall(msg.encode())
#             data = s.recv(1024)
#             print(f"Received data: {data.decode()}")
#         except socket.error:
#             break
#         except KeyboardInterrupt:
#             print("Connection closed")
#             break

# sel = selectors.DefaultSelector()

# hostname = socket.gethostname()
# messages = [b'connection successfull']

# def start_connections(host, port, conns):
#     server_addr = (host, port)
#     for i in range(0, conns):
#         connid = i + 1
#         print(f"Starting connection {connid}  to {server_addr}")

#         sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#         sock.setblocking(False)

#         sock.connect_ex(server_addr)
#         events = selectors.EVENT_READ | selectors.EVENT_WRITE

#         data = types.SimpleNamespace(
#             connid=connid,
#             msg_total=sum(len(m) for m in messages),
#             recv_total=0,
#             messages=messages.copy(),
#             outb=b"",
#         )

#         sel.register(sock,events,data=data)

# def service_connection(key, mask):
#     sock = key.fileobj
#     data = key.data
#     if mask & selectors.EVENT_READ:
#         recv_data = sock.recv(1024)  # Should be ready to read
#         if recv_data:
#             print(f"Received {recv_data.decode()} from connection {data.connid}")
#             data.recv_total += len(recv_data)
#         if not recv_data or data.recv_total == data.msg_total:
#             msg = input(f"{hostname}> ")
#             messages.append(msg.encode())
#             host, port, num_conns = sys.argv[1:4]
#             start_connections(host, int(port), int(num_conns))
#             # print(f"Closing connection {data.connid}")
#             # sel.unregister(sock)
#             # sock.close()
#     if mask & selectors.EVENT_WRITE:
#         if not data.outb and data.messages:
#             data.outb = data.messages.pop(0)
#         if data.outb:
#             print(f"Sending {data.outb!r} to connection {data.connid}")
#             sent = sock.send(data.outb)  # Should be ready to write
#             data.outb = data.outb[sent:]


# if len(sys.argv) != 4:
#     print(f"Usage: {sys.argv[0]} <host> <port> <num_connections>")
#     sys.exit(1)

# host, port, num_conns = sys.argv[1:4]
# start_connections(host, int(port), int(num_conns))

# try:
#     while True:
#         events = sel.select(timeout=1)
#         if events:
#             for key, mask in events:
#                 service_connection(key, mask)
#         # Check for a socket being monitored to continue.
#         if not sel.get_map():
#             break
# except KeyboardInterrupt:
#     print("Caught keyboard interrupt, exiting")
# finally:
#     sel.close()

# PART 2
import socket
import websocket

# async def hello(uri):
#     async with websockets.connect(uri) as websocket:
#         await websocket.send("Hello world")
#         greeting = await websocket.recv()
#         print(f"Recieved: {greeting}")

# asyncio.run(hello("ws://localhost:8765"))

hostname = socket.gethostname()
ws = websocket.WebSocket()
try:
    while True:
        msg = input(f"{hostname}> ")
        ws.connect("ws://localhost:8765")
        ws.send(msg)
        print(f"from {hostname}: {ws.recv()}")
except KeyboardInterrupt:
    print("Connection closed")