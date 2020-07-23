import socket
import os
from time import sleep

MCAST_GRP = '10.10.10.10'
MCAST_PORT = 9004
MULTICAST_TTL = 2
bytes_size_to_process = 1024

def startSocket():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MULTICAST_TTL)

    def sendDataOverSocket(data):
        print("Serving multicast data to: " + str(MCAST_GRP) + ":" + str(MCAST_PORT) +  " " + str(bytes_size_to_process) + " bytes")
        s.sendto(data, (MCAST_GRP, MCAST_PORT))

    print("Found " + str(os.stat('channels/LTVHD.tv').st_size) + " bytes file to stream. Waiting for clients...")

    while True:
        with open("channels/LTVHD.tv", "rb") as f:
            byte = f.read(bytes_size_to_process)
            sendDataOverSocket(byte)
            count = 0

            while byte:
                byte = f.read(bytes_size_to_process)
                sendDataOverSocket(byte)
                count += + bytes_size_to_process
                sleep(0.001)
                print("Bytes sent: " + str(count) + "/" + str(os.stat('channels/LTVHD.tv').st_size))
