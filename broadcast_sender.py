import socket
import time

# Define the broadcast address and port for sending messages
BROADCAST_IP = "192.168.0.255" 
PORT = 12345

def send_broadcast(message):

    # Create a socket for UDP communication
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Enable the socket to send broadcast messages
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    # Wait for 3 seconds before sending the message
    time.sleep(3)
    
    # Send the message to the broadcast address and port
    sock.sendto(message.encode(), (BROADCAST_IP, PORT))
    
    print(f"Sent broadcast message: {message}")

if __name__ == "__main__":
    send_broadcast("Hello, Cluster A!")
