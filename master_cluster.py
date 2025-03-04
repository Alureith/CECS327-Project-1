import socket
import time

def send_broadcast(message):
    broadcast_ip = '<broadcast>'  # Ensure this is set to the broadcast IP address of the network.
    port = 12345
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.sendto(message.encode(), (broadcast_ip, port))
    print(f"Sent message: {message}")

def broadcast_message_once():
    message = "Hello, Cluster A!"
    send_broadcast(message)

if __name__ == "__main__":
    # Ensure it only sends once
    broadcast_message_once()
