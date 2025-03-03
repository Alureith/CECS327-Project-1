import socket
import time

# Create a UDP socket using IPv4
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

# Enable socket option for port reuse, allowing multiple clients and servers to use the same port
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

# Enable broadcasting mode to send messages to all devices in the network
server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Set a timeout to prevent the socket from blocking forever when waiting for a response
server.settimeout(0.2)

# Define the message to be sent
message = b"Hello! This is a broadcast."

# Set the broadcast address for Cluster A 
broadcast_address = '192.168.100.255'  # Broadcast address for subnet 192.168.100.0/24

print("Server is broadcasting messages to all workers...")

while True:
    try:
        # Send the message to the broadcast address on port 37020
        server.sendto(message, (broadcast_address, 37020))
        print("Message sent!")
        time.sleep(1)  # Wait for 1 second before sending the next message
    except Exception as e:
        # If any exception occurs during sending, print the error
        print(f"Error occurred: {e}")
