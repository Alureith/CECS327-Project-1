import socket
import struct
import time

# Configuration
BROADCAST_PORT = 5007
MULTICAST_PORT = 5008
MCAST_GRP = '224.1.1.1'
BROADCAST_MESSAGE = b"Hello, Cluster A!"
MULTICAST_MESSAGE = b"Hello, Group B!"

# Broadcast - Sending
def send_broadcast():
    print("[Cluster A Master] Sending intra-cluster broadcast message: 'Hello, Cluster A!'")
    # Create a UDP socket for broadcasting
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # Enable broadcasting
    sock.sendto(BROADCAST_MESSAGE, ('<broadcast>', BROADCAST_PORT))
    print("Message sent!")
    time.sleep(1)

# Multicast - Sending
def send_multicast():
    print("[Cluster B Master] Sending intra-cluster multicast message: 'Hello, Group B!'")
    # Create a UDP socket for multicast
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)  # Set TTL to 2 hops
    sock.sendto(MULTICAST_MESSAGE, (MCAST_GRP, MULTICAST_PORT))
    print("Multicast message sent!")
    time.sleep(1)

# Broadcast - Receiving
def receive_broadcast():
    print("[Container] Listening for broadcast messages...")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('', BROADCAST_PORT))  # Bind to receive all broadcast messages
    while True:
        data, addr = sock.recvfrom(10240)
        print(f"Received broadcast message: {data}")

# Multicast - Receiving
def receive_multicast():
    print("[Container] Listening for multicast messages...")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('', MULTICAST_PORT))  # Bind to receive multicast messages on this port
    mreq = struct.pack('4sl', socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    while True:
        data, addr = sock.recvfrom(10240)
        print(f"Received multicast message: {data}")

# Run Broadcast and Multicast Communication
if __name__ == "__main__":
    send_broadcast()  # Send broadcast message
    send_multicast()  # Send multicast message
