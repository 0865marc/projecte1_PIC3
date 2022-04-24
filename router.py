import socket
import random
import time

##FUNCTIONS:
#Creates a list of file addresses
def addresses(filename): 
    with open(filename) as xfile:
        list_addresses = xfile.readlines()     #[127.0.0.1/n, 127.0.0.2/n, 127.0.1/n]

    for i in range(len(list_addresses)):
        list_addresses[i] = list_addresses[i][:-1]
   
    return list_addresses

#Choose a random address
def random_number(list_a): 
    address_choose = random.choice(list_a)
    address_choose = address_choose.strip('\n')
    
    return address_choose

#If the address is malformed, 
#   the router will send an error message to the client
def form_address(address): 
    list_address = address.split('.')
    list_correct = []
    result = True

    if len(list_address) != 4:
        list_correct.append(False)
    else: 
        for x in list_address:
            x = int(x)
            if x < 0 or x > 255:
               list_correct.append(False)
            else:
                list_correct.append(True)
        
    for x in list_correct:
        if x == False:
            result = False 

    return result

#Error Message
def error_message(result):
    if result == False:
        connection.send("Error Message: Address malformed".encode("utf_8"))

##Socket creation TCP 
sock_c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock_c.bind(("127.0.0.10",10000))##Bind Socket
sock_c.listen(1)
connection, client_address = sock_c.accept()#Receive data

##Socket creation UDP - communicate with the servers
sock_s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

shouldContinue = True
while shouldContinue:
    ##Receive the client petition
    data_c = connection.recv(50) #Data of client
    print("La opció triada pel client és: ", data_c.decode("utf-8"))

    ##Function call:
    three_addresses = addresses('addresses.txt')  #list of file addresses
    one_address_choose  = random_number(three_addresses) #Choose a random address
    print("Servidor aleatori escollit és: ", one_address_choose)
    isCorrect = form_address(one_address_choose) #Is the address correct?
    error_message(isCorrect) #Send error message

    if isCorrect ==  True:#If the address is correct it will send the request to the server

        sent_to_s = sock_s.sendto(data_c,(one_address_choose,10000)) #Send data to the server
        data_s, addres = sock_s.recvfrom(4096) #Recieve data from server
        msg = data_s.decode("UTF-8")
        print("Resposta rebuda del servidor: ", msg)

        if msg == "Exited":
            # Tancar la resta de servidors
            shouldContinue = False

            three_addresses.remove(one_address_choose)   # Eliminar el servidor que s'ha elegit aleatori de la llista, perque ja està tancat

            for adress in three_addresses: #For each address in the list
                if form_address(adress) == True: #If it is well formed
                    if adress != one_address_choose:
                        sent_to_s = sock_s.sendto(data_c,(adress,10000)) #Send data to the server

            sent_to_c = connection.send(data_s) #Send data to the client
            print("Bye")
            time.sleep(2)

        sent_to_c = connection.send(data_s) #Send data to the client
        print("\n")