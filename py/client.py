import socket
import time

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('51.11.50.70', 5050)

sock.connect(server_address)
# sock.setblocking(1)


def hex():
    msg = sock.recv(1024)
    a = []
    while msg:
        a.append(msg.decode("utf-8"))
        msg = sock.recv(1024)

    return a[1].splitlines()[-2]

hex()
sock.close()
