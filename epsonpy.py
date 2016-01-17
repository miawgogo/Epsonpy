import socket
import os
global s
global debugmode

def init(ip="127.0.0.1",port=3629,debug=False):
    debugmode = debug
    try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(ip, port)
    except exception as e:
        print e

def send(command):
    tcpbuff = 1024
    try:
        s.send(command)
        return s.recv(tcpbuff)
    except exception as e:
        print e

def source(action=):
    
