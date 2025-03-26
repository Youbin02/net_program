from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 3333))
s.listen(5)

print('waiting...')
while True:
    client, addr = s.accept()
    print('connection from ', addr)
    while True:
        form = client.recv(1024)
        if not form:
            break
        try:
            num1, cal, num2 = form.decode().split()
            num1 = int(num1)
            num2 = int(num2)
            if cal == '+':
                result = num1 + num2
            elif cal == '-':
                result = num1 - num2
            elif cal == '*':
                result = num1 * num2
            elif cal == '/':
                result = num1 / num2
                result = round(result, 1)
        except:
            client.send(b'Try again')
        else:
            client.send(str(result).encode())
    client.close()