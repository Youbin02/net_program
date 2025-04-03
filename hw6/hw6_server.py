import socket

BUFFSIZE = 1024
port = 2500

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))
mybox = {}
sendmsg = ''

while True:
    msg, addr = sock.recvfrom(BUFFSIZE)
    parts = msg.decode().split(' ', 2)
    
    opt = parts[0] if len(parts) > 0 else None
    mboxID = parts[1] if len(parts) > 1 else None
    message = parts[2] if len(parts) > 2 else None
    
    if opt == 'send':
        if mboxID not in mybox:
            mybox[mboxID] = [message]
        else:
            mybox[mboxID].append(message)
        
        sendmsg = "OK"
    
    elif opt == 'receive':
        if mboxID not in mybox:
            sendmsg = "No messages"
        else:
            if mybox[mboxID]:
                sendmsg = mybox[mboxID][0]
                mybox[mboxID].pop(0)
            else:
                sendmsg = "No messages"

    sock.sendto(sendmsg.encode(), addr)