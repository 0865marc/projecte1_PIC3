import socket

##Socket creation
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

##Send data
sock.connect(("127.0.0.10",10000))
sock.send("5".encode()) 

while True:
    a = sock.recv(50)  #Information received from the server
    if len(a) > 0:
        print(a)
        msg = a.decode("UTF-8")

        if msg == "Exited":
            break

#Falta: 1. que envii de manera aleatoria els numeros del 1 al 5
#2. quan el router li envii "error adreça mal formada", que ho torni a intentar X cops mes
#PER SI DE CAS LLEGEIXTE L'ENUNCIAT, PERO AIXO ES LO QUE MANAVA COMENTANT EL PROFE A CLASSE

