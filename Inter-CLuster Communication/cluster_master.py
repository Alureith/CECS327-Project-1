import socket
import sys

# Cluster Master IPs
CLUSTER_A_MASTER = "192.168.0.2"
CLUSTER_B_MASTER = "192.169.0.2"
PORT = 12346  # Use a separate port for inter-cluster communication

def cluster_master(is_cluster_a):
    master_ip = CLUSTER_A_MASTER if is_cluster_a else CLUSTER_B_MASTER
    peer_master_ip = CLUSTER_B_MASTER if is_cluster_a else CLUSTER_A_MASTER

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((master_ip, PORT))
    
    print(f"Cluster Master at {master_ip} listening for inter-cluster messages...", flush=True)

    while True:
        message, addr = sock.recvfrom(1024)
        print(f"Received message: {message.decode()} from {addr}", flush=True)

        # If it's from our own cluster, forward it to the other cluster master
        if addr[0] != peer_master_ip:
            print(f"Forwarding to cluster master {peer_master_ip}", flush=True)
            sock.sendto(message, (peer_master_ip, PORT))
        else:
            print("Delivering to final destination...", flush=True)

if __name__ == "__main__":
    import sys
    is_cluster_a = sys.argv[1] == "A"  # Run with argument "A" or "B"
    cluster_master(is_cluster_a)