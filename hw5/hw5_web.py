from socket import *

s = socket()
s.bind(('', 80))
s.listen(10)

while True:
    c, addr = s.accept()
    
    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')
    
    filename = req[0].split()
    filename = filename[1].lstrip("/")

    # 웹 서버 코드 작성
    if filename == 'index.html':
        f = open(filename, 'r', encoding='utf-8')
        mimeType = 'text/html'
    
    elif filename == 'iot.png':
        f = open(filename, 'rb')
        mimeType = 'image/png'
    
    elif filename == 'favicon.ico':
        f = open(filename, 'rb')
        mimeType = 'image/x-icon'
    
    # 각 객체(파일 또는 문자열) 전송 후, 소켓 닫기(c.close())
    res_msg = 'HTTP/1.1 200 OK\r\nContent-Type: ' + mimeType + '\r\n\r\n'
    c.send(res_msg.encode())
    
    if filename == 'index.html':
        data = f.read()
        c.send(data.encode('euc-kr'))
    
    elif filename == 'iot.png' or filename == 'favicon.ico':
        data = f.read()
        c.send(data)
    
    else:
        res_msg = 'HTTP/1.1 404 Not Found\r\n\r\n<HTML><HEAD><TITLE>Not Found</TITLE></HEAD><BODY>Not Found</BODY></HTML>'
        c.send(res_msg.encode())
    
    c.close()