import socket
import threading

def recv_handler(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break
            print(data.decode())
        except:
            break

server_addr = ('localhost', 2500)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(server_addr)

my_id = input("ID를 입력하세요: ")
sock.send(f"[{my_id}]".encode())

thread = threading.Thread(target=recv_handler, args=(sock,))
thread.daemon = True
thread.start()

while True:
    msg = input()
    if msg.lower() == 'quit':
        sock.send(f"[{my_id}] quit".encode())
        break
    sock.send(f"[{my_id}] {msg}".encode())

sock.close()
