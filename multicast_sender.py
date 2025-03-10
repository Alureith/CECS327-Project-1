import socket
import sys
import time

PORT = 12345

def send_multicast(message, multicast_group):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)

    time.sleep(5)

    sock.sendto(message.encode(), (multicast_group, PORT))
    print(f"Sent multicast message: {message} to {multicast_group}")

if __name__ == "__main__":
    # Use multicast group provided via command-line argument
    multicast_group = sys.argv[1] if len(sys.argv) > 1 else "224.1.1.1"
    send_multicast("Hello, Cluster B!", multicast_group)
