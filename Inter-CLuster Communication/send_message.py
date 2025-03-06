import socket
import sys

# Define the IP addresses of the cluster masters
CLUSTER_A_MASTER = "192.168.0.2" # Cluster A's master node IP
CLUSTER_B_MASTER = "192.169.0.2" # Cluster B's master node IP
PORT = 12346 # Port number for inter-cluster communication

def send_message(target_cluster, message):
    """
    Sends a message from a container to the target cluster via its master node.

    Args:
        target_cluster (str): "A" or "B", indicating which cluster the message is being sent to.
        message (str): The message to be sent.
    """
    # Determine which cluster master to send the message to
    sender_master_ip = CLUSTER_A_MASTER if target_cluster == "B" else CLUSTER_B_MASTER

    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Send the encoded message to the selected cluster master's IP and port
    sock.sendto(message.encode(), (sender_master_ip, PORT))
    print(f"Message sent to {sender_master_ip}: {message}")

if __name__ == "__main__":
    """
    Entry point of the script.
    Validates command-line arguments and sends a message to the specified cluster.
    """
     # Ensure the script is run with at least two arguments (target cluster and message)
    if len(sys.argv) < 3:
        print("Usage: python send_message.py <target_cluster> <message>")
        sys.exit(1) # Exit the script if incorrect usage
    # Extract target cluster from arguments
    target_cluster = sys.argv[1]
    # Extract message from arguments (joining in case of multiple words)
    message = " ".join(sys.argv[2:])
    # Call function to send message
    send_message(target_cluster, message)