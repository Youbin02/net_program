import socket
import select
import time

HOST = ''
PORT = 2500
BUFFER = 1024

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_sock.bind((HOST, PORT))
server_sock.listen(5)

sockets_list = [server_sock]
clients = {}

print(f"{PORT}번 포트에서 접속 대기 중...")

while True:
    read_sockets, _, _ = select.select(sockets_list, [], [])
    for sock in read_sockets:
        if sock == server_sock:
            client_socket, client_addr = server_sock.accept()
            sockets_list.append(client_socket)
            clients[client_socket] = client_addr
            print(f"새 클라이언트 접속: {client_addr}")
        else:
            try:
                data = sock.recv(BUFFER)
                if not data:
                    raise ConnectionResetError()
                message = data.decode()

                # 'quit' 처리
                if 'quit' in message:
                    print(f"{clients[sock]} exited")
                    sockets_list.remove(sock)
                    del clients[sock]
                    sock.close()
                    continue

                print(time.asctime() + f" {clients[sock]}: {message}")

                # 모든 클라이언트에게 전송
                for client in clients:
                    if client != sock:
                        try:
                            client.send(data)
                        except:
                            client.close()
                            sockets_list.remove(client)
                            del clients[client]
            except:
                print(f"클라이언트 {clients.get(sock)} 연결 종료")
                sockets_list.remove(sock)
                if sock in clients:
                    del clients[sock]
                sock.close()
