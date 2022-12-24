#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import time

msgFromClient = "Клиент подключен"
bytesToSend = msgFromClient.encode("utf-8")
serverAddressPort = ("127.0.0.1", 20001)
bufferSize = 1024
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPClientSocket.sendto(bytesToSend, serverAddressPort)
while True:
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    msg = "Текущая температура - {} С'".format(msgFromServer[0].decode("utf-8"))
    print(msg)
    time.sleep(10)
