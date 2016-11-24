#!/usr/bin/python
import socket
import platform
import sys
import threading

try:
    def socket_co():
        global s
        port = 999
        host = raw_input('Enter server address: ')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
except socket.error, (value, message):
    print "Socket error .... please resolve the problem as soon as you can !"
    s.close()
    sys.exit()

try:
    def data():
        system = platform.system()
        node = platform.node()
        version = platform.version()
        machine = platform.machine()
        f = s.makefile("r+")  # making file to store information ( as I think it do ) using the makefile()
        f.write('system: ' + str(system) + '\n')
        f.write('node: ' + str(node) + '\n')
        f.write('version: ' + str(version) + '\n')
        f.write('machine: ' + str(machine) + '\n')
        f.flush()
        sete = f.readlines()  # read lines from the file
        s.send(str(sete))
        s.close()
        sys.exit()  # end the operation
except:
    print ' Something went wrong .... '
    s.close()
    sys.exit()



def main():
    socket_co()
    data()


if __name__ == '__main__':
    main()
