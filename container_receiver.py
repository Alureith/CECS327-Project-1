import socket

def listen_for_message():
    port = 12345
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('0.0.0.0', port))  # Listening to all interfaces on this port

    # Listen for the message
    message, addr = sock.recvfrom(1024)
    print(f"Received broadcast message: {message.decode()}")

    # Close the socket after receiving the first message
    sock.close()

if __name__ == "__main__":
    listen_for_message()  # Only listen once
