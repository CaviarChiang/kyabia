import socket
import threading

port = 5000

s = socket.socket()

s.bind(('', port))

s.listen()

print("listening on port " + str(port))

def on_new_client(clientsocket,addr):
    print('starting new thread')
    count = 0
    while True:
        msg = clientsocket.recv(1024)
        print(str(addr) + ' >> ' + str(msg))
        response = 'Here is reponse number ' + str(count)
        count = count + 1
        #Maybe some code to compute the last digit of PI, play game or anything else can go here and when you are done.
        try:   
            clientsocket.send(response.encode('utf-8'))
        except:
            break
    print('thread broke')
    clientsocket.close()

while True:
    c, addr = s.accept()
    print("Connection from " + str(addr))
    t = threading.Thread(target=on_new_client, args=(c,addr))
    t.start()
 




