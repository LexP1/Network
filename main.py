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

data_out = b"GET / HTTP/1.1\r\nHost:ya.ru\r\n\r\n"
# b - двоичный вид
ya_sock.send(data_out)

# \r\n - перевод каретки
# \r\n\r\n - в конце два раза перевод каретки

data_in = ya_sock.recv(1024)
# по сколько байт она будет перехватывать на сетевой карте
# принимаем ответ в размере 1024 байта
# перехват записываем в переменную data_in
print(data_in)