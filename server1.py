#!/usr/bin/python
import socket
host = '192.168.1.107'
port = 1060
s = socket.socket()
s.bind((host,port)) #bind server
s.listen(2)
conn, addr = s.accept()
print addr , "Now Connected"
response =  conn.recv(1024)
print response
saved = open('saved_data.txt','w+')
saved.write(response)

conn.close()
