import socket
import time

# Broadcast IP address for the subnet (adjust according to your network)
BROADCAST_IP = "192.168.100.255"  # Broadcast IP address
PORT = 5000
MESSAGE = "Hello from the Master Node (Broadcast)"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # Enable broadcasting

print("Server is broadcasting messages to all workers...")

while True:
    try:
        # Send broadcast message to all containers in the subnet
        print(f"Sending broadcast message to {BROADCAST_IP}: {MESSAGE}")
        sock.sendto(MESSAGE.encode(), (BROADCAST_IP, PORT))  # Send message to broadcast IP
        print(f"Sent broadcast message: {MESSAGE}")
        time.sleep(5)  # Send message every 5 seconds
    except KeyboardInterrupt:
        print("Server shutting down.")
        break
    except Exception as e:
        print(f"Error: {e}")
        break
