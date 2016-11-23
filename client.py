#!/usr/bin/python
import socket
import platform
import  sys


def socket_co():
   port = 1060
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.connect(('192.168.1.107', port)) # my computer address and the port
   system = platform.system()
   node = platform.node()
   version = platform.version()
   machine = platform.machine()
   f = s.makefile("r+") #making file to store information ( as I think it do ) using the makefile()
   f.write('system: ' + str(system) + '\n')
   f.write('node: ' + str(node) + '\n')
   f.write('version: ' + str(version) + '\n')
   f.write('machine: ' + str(machine) + '\n')
   f.flush()
   sete = f.readlines() #read lines from the file
   s.send(str(sete))
   s.close()
   sys.exit() #end the operation


   def main():
       socket_co()

   if __name__ == '__main__':
       main()
