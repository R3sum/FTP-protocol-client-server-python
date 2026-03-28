# FTP-protocol-python

A simple file transfer system implemented in Python using TCP sockets.
This project demonstrates how file transfer protocols work at a low level,
similar to FTP but simplified.

---

## Features

- Multi-client support using threading
- File transfer over TCP sockets
- Simple client-server architecture

---

## How it works

The server listens for incoming connections and waits for file requests.
The client connects to the server, requests a file by name, and downloads it locally.

---

## Usage

Run the server first, then connect with the client.
```bash
python FTP-server.py
python FTP-client.py
```
