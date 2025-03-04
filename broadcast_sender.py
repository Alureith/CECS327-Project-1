import socket
import time

BROADCAST_IP = "192.168.0.255"  # Broadcast address for cluster_a
PORT = 12345

def send_broadcast(message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    time.sleep(3)
    
    sock.sendto(message.encode(), (BROADCAST_IP, PORT))
    print(f"Sent broadcast message: {message}")

if __name__ == "__main__":
    send_broadcast("Hello, Cluster A!")
