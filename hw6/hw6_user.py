from socket import *
import time

def log_data(device, data):
    timestamp = time.ctime()
    with open("data.txt", "a") as f:
        f.write(f"{timestamp}: {device}: {data}\n")

d1 = socket(AF_INET, SOCK_STREAM)
d2 = socket(AF_INET, SOCK_STREAM)
d1.connect(('localhost', 7777))
d2.connect(('localhost', 8888))

try:
    count1 = count2 = 0
    while count1 < 5 or count2 < 5:
        user_input = input("Enter 1(Device1), 2(Device2), or 'quit': ")
        
        if user_input == '1' and count1 < 5:
            d1.sendall(b'Request')
            data = d1.recv(1024).decode()
            log_data("Device1", data)
            count1 += 1
            print(f"Received from Device1: {data}")
        elif user_input == '2' and count2 < 5:
            d2.sendall(b'Request')
            data = d2.recv(1024).decode()
            log_data("Device2", data)
            count2 += 1
            print(f"Received from Device2: {data}")
        elif user_input == 'quit':
            d1.sendall(b'quit')
            d2.sendall(b'quit')
            break
        #else: print("Invalid input or maximum data collected from that device.")

finally:
    d1.close()
    d2.close()
