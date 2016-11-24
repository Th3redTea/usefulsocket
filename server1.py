#!/usr/bin/python
import socket
import sys
import threading


def hanlder():
    global s
    host = ' '
    port = 999
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', port))  # bind server
    s.listen(5)
    while True:
        conn, addr = s.accept()
        print addr, "Now Connected"
        response = conn.recv(1024)
        print  "recieved from " + str(addr[0])
        saved = open('saved_data.txt', 'w+')
        saved.write(response)  # store the received information in txt file
        while True:
            try:
                def client_handler():
                    teading = threading.Thread(target=hanlder())
                    teading.start()
                    print  response
                client_handler()
            except threading.ThreadError:
                print " Error while handilung thread"
                s.close()
                sys.exit()
        conn.close()


hanlder()
