import socket

PORT = 12345

def listen_for_broadcast():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    sock.bind(('', PORT))  # Listen on all interfaces

    print("Listening for broadcast messages...")
    
    message, addr = sock.recvfrom(1024)
    print(f"Received broadcast message: {message.decode()} from {addr}")

    sock.close()

if __name__ == "__main__":
    listen_for_broadcast()
