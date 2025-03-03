import socket
import struct
import time

MULTICAST_GROUP = '224.0.0.1'  # Multicast IP address for the group
PORT = 5000
MESSAGE = "Hello from the Master Node"

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Set TTL (Time To Live) for the multicast message (255 for global)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 255)

print("Server is sending messages to the multicast group...")

while True:
    try:
        # Send multicast message
        sock.sendto(MESSAGE.encode(), (MULTICAST_GROUP, PORT))
        print(f"Sent to multicast group {MULTICAST_GROUP}: {MESSAGE}")
        time.sleep(5)  # Send message every 5 seconds
    except KeyboardInterrupt:
        print("Server shutting down.")
        break
    except Exception as e:
        print(f"Error: {e}")
        break
