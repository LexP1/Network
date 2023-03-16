import socket

'''
Скринкаст к 6 семинару по сетям
Пример создания сокета
Пример посыла запроса
'''

ya_sock = socket.socket()
addr = ("77.88.55.242", 443)
# AF_INET = IPv4
ya_sock.connect(addr)
# addr = (ip адрес, port)