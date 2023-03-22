import socket
import threading

sock = socket.socket()
addr = ("158.160.19.47", 55555)
sock.connect(addr)

def socketSend(data):
    sock.send(data)

def socketReceive():
    while True:
        data_in = sock.recv(1024)
        print(data_in.decode('ascii'))

rec_thread = threading.Thread(target=socketReceive)
rec_thread.start()

# GET / HTTP/1.1\r\nHost:158.160.19.47\r\n\r\n")

while True:
    data = input()
    socketSend(f"Alex: {data}".encode('ascii'))

# sock.close()
