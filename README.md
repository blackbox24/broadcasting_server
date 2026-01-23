
https://roadmap.sh/projects/broadcast-server

# Broadcast Chat Server & Client

A simple, lightweight **real-time broadcast chat** application implemented in Python using TCP sockets.  
One server broadcasts every message it receives to **all connected clients** (classic chatroom behavior).

## Features

- Start a chat server with one command
- Connect multiple clients to the server
- Messages sent by any client are instantly broadcast to everyone else
- Tracks connected users in a `clients.json` file
- Graceful handling of client disconnections
- Threaded client handling (supports multiple simultaneous users)
- Basic command-line interface

## Requirements

- Python 3.6+
- No external dependencies (only standard library modules)

## Installation

```bash
# Clone the repository (or just download the files)
git clone https://github.com/yourusername/broadcast-chat.git
cd broadcast-chat
```

No `pip install` is required — everything uses built-in Python libraries.

## Project Structure

```
broadcast-chat/
├── server.py          # Main server logic + client handling
├── client.py          # Simple interactive chat client
├── helpers.py         # JSON file read/write utilities
└── clients.json       # Stores list of currently connected users (auto-created)
```

## Usage

### 1. Start the Server

```bash
python server.py
```

Or (if you later add argparse / CLI entry point):

```bash
python broadcast.py start
# or
broadcast-server start
```

Default listen address: `127.0.0.1:5000`

You should see:

```
Server running on 127.0.0.1:5000
```

### 2. Connect a Client

Open a new terminal and run:

```bash
python client.py
```

You'll be prompted with your hostname:

```
DESKTOP-ABC123> 
```

Type a message and press Enter — it will be sent to everyone.

### Example Session

**Terminal 1** (server)

```
Server running on 127.0.0.1:5000
('127.0.0.1', 54321) connected to server
('127.0.0.1', 54322) connected to server
```

**Terminal 2** (client 1)

```
DESKTOP-ALICE> Hello everyone!
```

**Terminal 3** (client 2)

```
LAPTOP-BOB> Hello everyone!
Msg: Hello everyone!
LAPTOP-BOB> I'm here too
```

**Terminal 2** sees:

```
Msg: Hello everyone!
Msg: I'm here too
```

## Planned / Possible Improvements

- Add nickname / username registration
- Proper CLI with `argparse` (`broadcast-server start --port 5555 --host 0.0.0.0`)
- Timestamp messages
- Show who sent each message
- Support for private messages
- Colors in terminal output
- Graceful server shutdown (close all client sockets)
- Better error messages and reconnection logic

## Current Limitations

- No authentication
- Messages are broadcast without sender name
- Very basic disconnection handling
- Hardcoded host/port (127.0.0.1:5000)
- `clients.json` is overwritten on every change (not atomic)

## License

MIT License

Feel free to use, modify, and share.

---

Made with pure Python sockets • 2025
