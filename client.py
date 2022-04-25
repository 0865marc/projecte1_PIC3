import socket

def check_input(number):
    if int(number) in list(range(1,6)):
        print("La opció triada pel client és valida : ", number)
        return True
    else:
        print("La opció triada pel clien NO és valida : ", number)
        return False

##Socket creation
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

##Send data
sock.connect(("127.0.0.10",10000))

shouldContinue = True
while shouldContinue:
    # Loop until a valid choice by the user is given
    while True:
        print("\n------------------------------------------------")
        number=input("What do you want to do?\n1-Number of Mails\n2-Get a Mail\n3-Number of books\n4-Get a book\n5-Exit the program\n")
        isCorrect = check_input(number)
        if isCorrect:
            break

    tries = 1

    while tries<=3:
        print("Intent numero: ", tries)
        sock.send(number.encode("utf_8"))
        a = sock.recv(10000)
        msg= a.decode("UTF-8") 
        tries += 1

        if msg != "Error Message: Address malformed" and msg != "Exited":
            # Si la resposa NO és un error, printeja la resposta i surt del bucle per tornar a demanar quina será la següent accio
            print("Resposta rebuda del router: ", msg)
            break
        
        elif msg == "Exited":
            sock.close()
            print('See you soon')
            shouldContinue = False
            break

        else:
            print("Adress malformed")
    



        
        



                

