import socket
 
msgFromClient       = "Hello UDP Server"
bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = ("192.168.88.36", 9004)
bufferSize          = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket
UDPClientSocket.sendto(bytesToSend, serverAddressPort)

count = 0
while True:
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    count += 1
    print(count * 1024)
    with open("LTVHD.tv", "ab") as f:
        f.write(msgFromServer[0])
