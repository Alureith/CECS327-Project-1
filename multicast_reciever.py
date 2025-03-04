import socket
import struct
import sys

PORT = 12345
TIMEOUT = 10  # Exit after 10 seconds if no message is received

def listen_multicast(multicast_group):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind to all interfaces on the correct port
    sock.bind(('', PORT))

    # Join multicast group
    multicast_request = struct.pack("4sL", socket.inet_aton(multicast_group), socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, multicast_request)

    # Set timeout for receiving
    sock.settimeout(TIMEOUT)

    print(f"Listening for multicast messages on {multicast_group}... (Will exit after {TIMEOUT}s if no message is received)")

    try:
        message, addr = sock.recvfrom(1024)
        print(f"Received multicast message: {message.decode()} from {addr}")
    except socket.timeout:
        print(f"No message received in {TIMEOUT} seconds. Exiting...")

    sock.close()

if __name__ == "__main__":
    # Use multicast group provided via command-line argument
    multicast_group = sys.argv[1] if len(sys.argv) > 1 else "224.1.1.1"
    listen_multicast(multicast_group)
