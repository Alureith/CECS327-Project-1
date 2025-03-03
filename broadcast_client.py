import socket

# Create a UDP socket using IPv4
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

# Enable socket option for port reuse, allowing multiple clients and servers to use the same port
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

# Enable broadcasting mode to send messages to all devices in the network
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Bind the client to the specified port (37020) on all available interfaces
client.bind(("", 37020))

print("Listening for broadcast messages...")

while True:
    try:
        # Receive a message from the server
        data, addr = client.recvfrom(1024)  # Buffer size of 1024 bytes
        print("Received message: %s" % data)
    except socket.timeout:
        # In case of a timeout (if you implement one), this block will execute
        print("Timeout occurred")
