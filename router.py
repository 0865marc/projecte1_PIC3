import socket
import random
import time

### STEP 1
##Socket creation TCP - receive the client petition  
sock_c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock_c.bind(("127.0.0.10",10000))##Bind Socket
sock_c.listen(1)
connection, client_address = sock_c.accept()#Receive data
data_c = connection.recv(50) #Data of client

### STEP 2
##Socket creation UDP - communicate with the servers
sock_s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

### STEP 3 - table of routes with 3 addresses
def addresses(filename):
    with open(filename) as xfile:
        list_addresses = xfile.readlines()
   
    return list_addresses

### STEP 4.a - choose a random address
def random_number(list_a):
    address_choose = random.choice(list_a)
    address_choose = address_choose.strip('\n')
    
    return address_choose

### STEP 4.b - If the address is malformed, the router will send an error message to the client
def malformed(address):
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

def error_message(result):
    if result == False:
        connection.send("Error Message: Address malformed".encode("utf_8"))

three_addresses = addresses('addresses.txt')
one_address_choose  = random_number(three_addresses)
#print(one_address_choose)
#print(len(one_address_choose))
address_is_malformed = malformed(one_address_choose)
e_message = error_message(address_is_malformed)

### STEP 4.c - If the address is correct it will send the request to the server
while True:
    if address_is_malformed ==  True:
        sent_to_s = sock_s.sendto(data_c,(one_address_choose,10000)) #Send data to the server

        data_s, addres = sock_s.recvfrom(4096) #Data of server
        msg = data_s.decode("UTF-8")

        if msg == "Exited":
            sent_to_c = connection.send(data_s) #Send data to the client
            time.sleep(1)
            print("adeu")
            break

        sent_to_c = connection.send(data_s) #Send data to the client