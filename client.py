import socket

##Socket creation
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

##Send data
sock.connect(("127.0.0.10",10000))

while True:
    print("What do you want to do?\n1-Number of Mails\n2-Get a Mail\n3-Number of books\n4-Get a book\n5-Exit the program\n")
    number=input()
    i=1
    print(i)
    #Information received from the server
    x = range(1, 4)
    if 1<= i and i <=3:
        sock.send(number.encode()) 
        print("enviat")
        a = sock.recv(10000)
        print("rebut")
        msg = a.decode("UTF-8") 
        print(i)
        if len(a) > 0:
            if msg == "Exited":
                print('See you soon')
                sock.close()
                break
            elif msg == "Error Message: Address malformed":
                print(msg)
                sock.send(number.encode()) 
                i+=1
                print(i)
            else:
                print(msg)
                i=6
                print(i)

                

