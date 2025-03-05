import socket
import sys

CLUSTER_A_MASTER = "192.168.0.2"
CLUSTER_B_MASTER = "192.169.0.2"
PORT = 12346

def send_message(target_cluster, message):
    sender_master_ip = CLUSTER_A_MASTER if target_cluster == "B" else CLUSTER_B_MASTER

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(message.encode(), (sender_master_ip, PORT))
    print(f"Message sent to {sender_master_ip}: {message}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python send_message.py <target_cluster> <message>")
        sys.exit(1)
    
    target_cluster = sys.argv[1]
    message = " ".join(sys.argv[2:])
    send_message(target_cluster, message)