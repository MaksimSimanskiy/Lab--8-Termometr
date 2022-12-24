#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import random
import time

localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))
print("Термометр работает")


def temp():
    return str(random.randint(18, 30))


while True:
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0].decode("utf-8")
    address = bytesAddressPair[1]
    print("Сообщение от клиента:{}".format(message))
    print("IP клиента:{}".format(address))
    while True:
        time.sleep(1)
        current_temp = temp()
        print("Показания термометра - " + current_temp)
        UDPServerSocket.sendto(current_temp.encode("utf-8"), address)
