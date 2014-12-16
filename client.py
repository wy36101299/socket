#-*- coding: UTF-8 -*- 
import sys
import socket
HOST='localhost'
PORT = int(sys.argv[1])

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)      
s.connect((HOST,PORT))       # 依照 HOST PORT連接server
while 1:
       cmd=raw_input("Please input cmd:")       #輸入傳給server的data
       s.sendall(cmd)      #把data發送給server
       data=s.recv(1024)     #把接收的數據變為變數data
       print data         #print data
s.close()   #關閉連線