import socket
import os
import sys
import time
from time import sleep

MCAST_GRP = '10.10.10.10'
MCAST_PORT = 9004
MULTICAST_TTL = 10
bytes_size_to_process = 4096
time_between_data_seconds = 5

def startSocket():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MULTICAST_TTL)

    def sendDataOverSocket(data):
        if data:
            bytes_size_to_process = sys.getsizeof(data)

            print("Serving UDP multicast data to: " + str(MCAST_GRP) + ":" + str(MCAST_PORT) +  " " +
                  str(bytes_size_to_process) + " bytes" +
                  " (file size: " + str(os.stat('channels/currentFile.ts').st_size) + ")")

            s.sendto(data, (MCAST_GRP, MCAST_PORT))
            sleep(0.005)

    def waitForNewData(start, end):
        result = (time_between_data_seconds - (end-start))
        if result < 0:
            print("No sleep needed we are {} seconds late to stream data!".format(result))
            return 0
        else:
            print("Sleeping for {} Waiting for next data...".format(result))
            return result

    while True:
        starttime = time.time()
        with open("channels/currentFile.ts", "rb", buffering=1) as f:
            byte = f.read(bytes_size_to_process)
            sendDataOverSocket(byte)

            while byte:
                byte = f.read(bytes_size_to_process)
                sendDataOverSocket(byte)

            f.close()
            endtime = time.time()
            sleep(waitForNewData(starttime, endtime))