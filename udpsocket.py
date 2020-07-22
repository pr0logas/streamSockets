import socket
import os

def startSocket():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('0.0.0.0', 9004))
    bytes_size_to_process = 1024

    def sendDataOverSocket(data):
            print("Sending data to " + str(address) + " " + str(bytes_size_to_process) + " bytes")
            s.sendto(data, address)

    print("Found " + str(os.stat('channels/LTVHD.tv').st_size) + " bytes file to stream. Waiting for clients...")

    while True:
        data, address = s.recvfrom(1)

        if address:
            count = 0
            print("Got a new client! " + str(address) + " Preparing to serve the data...")
            with open("channels/LTVHD.tv", "rb") as f:
                byte = f.read(bytes_size_to_process)
                sendDataOverSocket(byte)
                while byte:
                    byte = f.read(bytes_size_to_process)
                    sendDataOverSocket(byte)
                    count += + bytes_size_to_process
                print(count)