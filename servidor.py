#%%
import socket
import os
import random

#%%
#port = input("introdueix el port")

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind(("127.0.0.11", 10000))



while True:
    data, adress = socket.recvfrom(4096)

    msg = data.decode("UTF-8")

    if msg[0] == "1":
        # Count number of mails
        n_mails = len(os.listdir("mails"))
        sent = socket.sendto(n_mails.encode(), adress)      ##convertir n_mails a bytes

    elif msg[0] == "2":
        # Return random mail
        mails = os.listdir("mails")
        random_mail = mails[random.randint(0, len(mails)-1)]
        with open("mails/" + random_mail) as f:
            content = f.read()
        sent = socket.sendto(content.encode(), adress)      ##convertir content a bytes

    elif msg[0] == "3":
        # Count number of books
        n_books = len(os.listdir("books"))
        sent = socket.sendto(n_books.encode(), adress)      ##convertir n_books a bytes

    elif msg[0] == "4":
        # Return random book
        books = os.listdir("books")
        random_book = books[random.randint(0, len(books)-1)]
        with open("mails/" + random_book) as f:
            content = f.read()
        sent = socket.sendto(content.encode(), adress)       ##convertir content a bytes

    elif msg[0] == "5":
        # Exit execution
        sent = socket.sendto("Exited", adress)      #convertir "Exited" a bytes
        break

    else:
        print("Error, try again")

