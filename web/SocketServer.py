# -*- coding: utf-8 -*-
###########################################
import socket
import threading
import time

def tcplink(sock, addr):
    print('Accept new connection from %s:%s' % addr)
    sock.send(b'welcome. input "exit" to exit')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 9999
s.bind(('127.0.0.1', port))
s.listen(5)  # 5 is backlog
print('waiting for connection: 127.0.0.1:%d' % port)
while True:
    sock, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()

