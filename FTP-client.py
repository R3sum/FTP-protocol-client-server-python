import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9090))

def download():
    while True:
        filename = input('Enter filename with extension(enter exit to quit): ').strip()
        s.send(filename.encode('utf-8'))
        if filename.lower() == 'exit':
            break
        response = s.recv(1024).decode('utf-8')
        if response == 'file not found':
            print('\nFile not found, try again.\n')
            continue
        try:
            size = int(response)
        except ValueError:
            print(f'\nUnexpected response: {response}\n')
            continue
        data = b''
        while len(data) < size:
            chunk = s.recv(4096)
            if not chunk:
                break
            data += chunk
        try:
            output = f'download_{filename}'
            with open(output, 'wb') as f:
                f.write(data)
            print(f'\nFile saved as: {output}\n')
        except Exception as e:
            print(f'\nError saving file: {e}\n')
            continue
        again = input('Download another file? (y/n): \n').strip().lower()
        if again != 'y':
            break
    s.close()

threading.Thread(target=download).start()