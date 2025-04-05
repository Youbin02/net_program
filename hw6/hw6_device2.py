from socket import *
import random

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 8888))
s.listen()

def generate_data():
    heartbeat = random.randint(40, 140)
    steps = random.randint(2000, 6000)
    cal = random.randint(1000, 4000)
    return f"Heartbeat={heartbeat}, Steps={steps}, Cal={cal}"

while True:
    print("Device2 is waiting for connection...")
    conn, addr = s.accept()
    with conn:
        #print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024).decode()
            if data == 'Request':
                response = generate_data()
                conn.sendall(response.encode())
            elif data == 'quit':
                #print("Device2 shutting down.")
                break
