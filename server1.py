#!/usr/bin/python
import socket
import  sys
host = ' '
port = 1060
s = socket.socket()
s.bind(('',port)) #bind server
s.listen(2)
conn, addr = s.accept()
print addr , "Now Connected"
response =  conn.recv(1024)
print response
saved = open('saved_data.txt','w+')
saved.write(response) # store the received information in txt file

conn.close()