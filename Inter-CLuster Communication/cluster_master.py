import socket
import sys

# Cluster Master IPs
CLUSTER_A_MASTER = "192.168.0.2" # IP address of Cluster A's master node
CLUSTER_B_MASTER = "192.169.0.2" # IP address of Cluster B's master node
PORT = 12346  # port number for inter-cluster communication

def cluster_master(is_cluster_a):
    """
    Function to handle message routing for a cluster master.
    - Listens for incoming messages.
    - Forwards messages to the peer cluster master when needed.
    - Delivers messages to the final destination if necessary.

    Args:
        is_cluster_a (bool): True if this is the master for Cluster A, False if for Cluster B.
    """
    # Determine the IP address of this cluster master and its peer
    master_ip = CLUSTER_A_MASTER if is_cluster_a else CLUSTER_B_MASTER
    peer_master_ip = CLUSTER_B_MASTER if is_cluster_a else CLUSTER_A_MASTER

    # Create a UDP socket for communication
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Bind the socket to the master node's IP and designated port
    sock.bind((master_ip, PORT))
    
    print(f"Cluster Master at {master_ip} listening for inter-cluster messages...", flush=True)

    while True:
        # Receive a message (max 1024 bytes) and the sender's address
        message, addr = sock.recvfrom(1024)
        print(f"Received message: {message.decode()} from {addr}", flush=True)

        # If it's from our own cluster, forward it to the other cluster master
        if addr[0] != peer_master_ip:
            print(f"Forwarding to cluster master {peer_master_ip}", flush=True)
            sock.sendto(message, (peer_master_ip, PORT))
        else:
            print("Delivering to final destination...", flush=True)

if __name__ == "__main__":
    """
    Entry point of the script.
    Determines whether the current instance is for Cluster A or B
    based on the command-line argument.
    """
    is_cluster_a = sys.argv[1] == "A"  # Run with argument "A" or "B"
    cluster_master(is_cluster_a)