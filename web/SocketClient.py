# -*- coding: utf-8 -*-
###########################################
import socket

print('start to run socket client')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
print(s.recv(1024).decode('utf-8'))

while True:
    # # data = b'luke'
    # data = input('input data to send to server: ')
    # data = bytes(data, encoding='utf-8')
    # s.send(data)
    # print(s.recv(1024).decode('utf-8'))
    # break

    data = input('input data to send to server: ')
    data = bytes(data, encoding='utf-8')
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
    if (data == b'exit'):
        break
s.close()

print('end: socket client')
