#Server program
import sys 
import socket

#creates connection, socket
def soketmake():
    try:
        global host
        global port
        global s
        host = ''
        port = 9000
        s = socket.socket()
    except socket.error as msg:
        print('Socket had an error lol' + str(msg))
        

#bind socket to port
def socketbid():
    try:
        global host
        global port
        global s 
        print('binding ur socket to some port:>' + str(port))
        s.bind((host, port))
        s.listen(5)#amount of bad connections which can be taken becuser 
    except socket.error as msg:
        print('lol u fucked up i cba it might retry it might not\n retrying noe ')
        socketbid()


#make some connection via listening and stuff
def socketaccept():
    conn, address = s.accept()#info here
    print('going to accept now...\nconnection established mad shit ' +'IP:' + address[0] + ', port:' + str(address[1]))
    sendcommand(conn)#now waits for ur commands
    conn.close()

def sendcommand(conn):
    while True:
        cmd = input()#now takes input from our terminal
        if cmd == 'quit':#if u wanna quit type this in terminal
            conn.close()
            s.close()
            sys.exit()#command just makes u leave innit
        if len(str.encode(cmd)) > 0:#sends bytes
            conn.send(str.encode(cmd))
            clientreponse = str(conn.recv(1024), 'utf-8')#response we get in bytes gets encoded insome charencoder i did utf8 cos
            print(clientreponse, end = '')


def everything():
    soketmake()
    socketbid()
    socketaccept()
    sendcommand()

everything()
#end of server program