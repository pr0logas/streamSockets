import socket
import os, sys, time
from time import sleep

MCAST_GRP = '10.10.10.10'
MCAST_PORT = 9004
MULTICAST_TTL = 10
bytes_size_to_process = 1024
time_between_data_seconds = 5
time_between_packets_float = 0.0055

def startSocket():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MULTICAST_TTL)

    def sendDataOverSocket(data, sleeptime):
        if data:
            bytes_size_to_process = sys.getsizeof(data)

            #print("Serving UDP multicast data to: " + str(MCAST_GRP) + ":" + str(MCAST_PORT) +  " " +
            #      str(bytes_size_to_process) + " bytes" +
            #      " (file size: " + str(os.stat('channels/currentFile.ts').st_size) + ")")

            s.sendto(data, (MCAST_GRP, MCAST_PORT))
            sleep(sleeptime)

    def adjustTimeForNewData(start, end, sleeptime):
        result = (time_between_data_seconds - (end-start))
        if result < 0:
            print("No sleep needed we are {} seconds late to stream the data!".format(result) + " Next sleep: " + str(sleeptime))
        else:
            print("Sleeping for {} Waiting for next data...".format(result) + " Next sleep: " + str(sleeptime))

    while True:

        starttime = time.time()

        with open("channels/currentFile.ts", "rb", buffering=1) as f:
            byte = f.read(bytes_size_to_process)
            expectedPackets = os.stat('channels/currentFile.ts').st_size / bytes_size_to_process
            print(expectedPackets)
            sleepTime = (time_between_data_seconds / expectedPackets) - 0.000120256
            sendDataOverSocket(byte, sleepTime)

            while byte:
                byte = f.read(bytes_size_to_process)
                sendDataOverSocket(byte, sleepTime)

            f.close()

            endtime = time.time()
            adjustTimeForNewData(starttime, endtime, sleepTime)
            #sleep(time_between_packets_float)