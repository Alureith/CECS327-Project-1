import socket
import time

PORT = 5000
BUFFER_SIZE = 1024

# Create the UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind to all interfaces to listen for broadcast messages on port 5000
sock.bind(("", PORT))

print("Listening for broadcast messages...")

while True:
    try:
        # Receive the data sent to the broadcast address
        data, addr = sock.recvfrom(BUFFER_SIZE)
        print(f"Received message: {data.decode()} from {addr}")
        time.sleep(1)  # Keeps the script alive and continues listening
    except Exception as e:
        print(f"Error: {e}")
        break
