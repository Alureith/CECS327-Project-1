import socket

# Define the port number to listen for messages
PORT = 12345

def listen_for_broadcast():

    # Create a socket for UDP communication
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Allow the socket to be reused to avoid errors
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Bind the socket to listen on the specified port and all network interfaces
    sock.bind(('', PORT)) 

    print("Listening for broadcast messages...")
    
    # Receive the message and the address it came from
    message, addr = sock.recvfrom(1024)
   
    print(f"Received broadcast message: {message.decode()} from {addr}")

    sock.close()

if __name__ == "__main__":
    listen_for_broadcast()
