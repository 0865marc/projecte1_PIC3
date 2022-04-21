import socket
import random
import time

##FUNCTIONS:
#Creates a list of file addresses
def addresses(filename): 
    with open(filename) as xfile:
        list_addresses = xfile.readlines()
   
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

##Socket creation UDP - communicate with the servers
sock_s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    ##Receive the client petition
    sock_c.listen(1)
    print("escoltant")
    connection, client_address = sock_c.accept()#Receive data
    print('receive')
    data_c = connection.recv(50) #Data of client
    print(data_c)

    ##Function call:
    three_addresses = addresses('addresses.txt')  #list of file addresses
    one_address_choose  = random_number(three_addresses) #Choose a random address
    print(one_address_choose)
    correct_or_malformed = form_address(one_address_choose) #Is the address malformed?
    e_message = error_message(correct_or_malformed) #Send error message

    if correct_or_malformed ==  True:#If the address is correct it will send the request to the server
        sent_to_s = sock_s.sendto(data_c,(one_address_choose,10000)) #Send data to the server

        data_s, addres = sock_s.recvfrom(4096) #Data of server
        msg = data_s.decode("UTF-8")

        if msg == "Exited":
            for i in three_addresses: #For each address in the list
                if form_address(i) == True: #If it is well formed
                    print(i)
                    sent_to_s = sock_s.sendto(data_c,(i,10000)) #Send data to the server

            sent_to_c = connection.send(data_s) #Send data to the client
            time.sleep(2)
            print("Bye")
            break

        sent_to_c = connection.send(data_s) #Send data to the client