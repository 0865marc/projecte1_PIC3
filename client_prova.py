import socket

##Socket creation
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

##Send data
sock.connect(("127.0.0.10",10000))
sock.send("5".encode()) #"utf_8"

while True:
    a = sock.recv(50)
    if len(a) > 0:
        print(a)
        msg = a.decode("UTF-8")

        if msg == "Exited":
            break



