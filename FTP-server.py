import socket
import threading
import os

i=0
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

while True:
    try:
        n_client = int(input('Max clients: '))
    except:
        print('\ninteger number only, retry\n')
        continue
    break

s.bind(('0.0.0.0', 9090))
s.listen(n_client)
print('\nServer waiting for connections...\n')


def send_file(filename, cs):
    filename = filename.strip()
    if not os.path.exists(filename):
        cs.send('file not found\n'.encode('utf-8'))
        return
    try:
        size = os.path.getsize(filename)
        cs.send(str(size).encode('utf-8'))
        with open(filename, 'rb') as f:
            while True:
                chunk = f.read(4096)
                if not chunk:
                    break
                cs.send(chunk)
        print(f'File "{filename}" sent successfully.\n')
    except Exception as e:
        print(f'Error sending file: {e}\n')

def client_handler(cs, addr):
    while True:
        try:
            message = cs.recv(1024).decode('utf-8').strip()
            if not message or message.lower() == 'exit':
                print(f'Client {addr} disconnected.\n')
                break
            print(f'[{addr}] Requested file: "{message}"\n')
            send_file(message, cs)
        except ConnectionResetError:
            print(f'Connection with {addr} terminated.\n')
            break
        except Exception as e:
            print(f'Error with {addr}: {e}\n')
            break
    cs.close()

for i in range(n_client):
    cs, addr = s.accept()
    print(f'New connection from {addr}\n')
    threading.Thread(target=client_handler, args=(cs, addr)).start()
    
print('max number of client reached\n')