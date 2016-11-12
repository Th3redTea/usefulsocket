#!/usr/bin/python
import socket
import platform
system   = platform.system()
node     = platform.node()
release  = platform.release()
version  = platform.version()
machine  = platform.machine()
processor= platform.processor()





s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.1.107"  # server address
port = 1060 #server port
s.connect((host,port))
s.send('system: '+str(system)+'\n')
s.send('node: '+str(node)+'\n')
s.send('release: '+str(release)+'\n')
s.send('version: '+str(version)+'\n')
s.send('machine: '+str(machine)+'\n')

s.close()
