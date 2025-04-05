from socket import *
import random

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 7777))
s.listen()

def generate_data():
    temp = random.randint(0, 40)
    humid = random.randint(0, 100)
    illum = random.randint(70, 150)
    return f"Temp={temp}, Humid={humid}, Illum={illum}"

while True:
    print("Device1 is waiting for connection...")
    conn, addr = s.accept()
    with conn:
        #print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024).decode()
            if data == 'Request':
                response = generate_data()
                conn.sendall(response.encode())
            elif data == 'quit':
                #print("Device1 shutting down.")
                break
