import socket

port = input("introdueix el port")

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind(("127.0.0.1", port))

data, adress = socket.recvfrom(4096)

msg = data.decode("UTF-8")


if msg[0] == "1":
    pass
elif msg[0] == "1":
    pass
elif msg[0] == "2":
    pass

