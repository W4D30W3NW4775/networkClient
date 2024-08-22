#!/usr/bin/python3

import socket

#establish a connection and connect using IP and port.
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("IP", Port))

#receive data, split string and save values in variables
print(s.recv(1024).decode())
recv_string = s.recv(1024).decode().split()
value1 = recv_string[8]
value2 = recv_string[10]
value3 = recv_string[12]

#do the math and cast result into string
result = (int(value1)+int(value2))*int(value3)
cast_result = str(result)

#send result back, receive and print message and close connection
s.send(cast_result.encode())
print(s.recv(1024).decode())
s.close()
