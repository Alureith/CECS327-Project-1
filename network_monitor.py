import csv
import time
from scapy.all import sniff, IP, TCP, UDP

LOG_FILE = "/app/logs/network_traffic_log.csv"

# Define cluster IP ranges
CLUSTER_A_RANGE = "192.168.0."
CLUSTER_B_RANGE = "192.169.0."

# Define protocol mapping
PROTOCOL_MAP = {6: "TCP", 17: "UDP"}

# Define flag mapping for TCP packets
TCP_FLAG_MAP = {
    "S": "SYN",
    "A": "ACK",
    "F": "FIN",
    "R": "RST",
    "P": "PSH",
    "U": "URG",
}

def extract_flags(tcp_flags):
    """Extract TCP flags and return a hex representation."""
    flags = []
    for flag in TCP_FLAG_MAP.keys():
        if flag in tcp_flags:
            flags.append(TCP_FLAG_MAP[flag])
    return hex(int(tcp_flags))

def packet_callback(packet):
    """Callback function to process captured packets."""
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto
        length = len(packet)

        # Identify protocol
        protocol = PROTOCOL_MAP.get(proto, "OTHER")

        # Identify intra-cluster or inter-cluster communication
        if src_ip.startswith(CLUSTER_A_RANGE) and dst_ip.startswith(CLUSTER_A_RANGE):
            comm_type = "Intra-Cluster"
            cluster_src = "Cluster A"
            cluster_dst = "Cluster A"
        elif src_ip.startswith(CLUSTER_B_RANGE) and dst_ip.startswith(CLUSTER_B_RANGE):
            comm_type = "Intra-Cluster"
            cluster_src = "Cluster B"
            cluster_dst = "Cluster B"
        else:
            comm_type = "Inter-Cluster"
            cluster_src = "Cluster A" if src_ip.startswith(CLUSTER_A_RANGE) else "Cluster B"
            cluster_dst = "Cluster B" if dst_ip.startswith(CLUSTER_B_RANGE) else "Cluster A"

        # Handle TCP flags
        flags_hex = "0x000"
        if protocol == "TCP" and TCP in packet:
            flags_hex = extract_flags(packet[TCP].flags)

        # Log data
        log_entry = [
            comm_type,
            f"{time.time():.6f}",  # Timestamp in seconds
            cluster_src,
            cluster_dst,
            src_ip,
            dst_ip,
            protocol,
            length,
            flags_hex
        ]

        # Print captured packet info
        print(f"📡 {comm_type}: {src_ip} → {dst_ip} [{protocol}] Length: {length} Flags: {flags_hex}")

        # Ensure logs are written to the file immediately
        with open(LOG_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(log_entry)
            f.flush()  # 👈 Force the file to update immediately


def setup_logging():
    """Initialize the log file with headers."""
    with open(LOG_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Type", "Time (s)", "Source Cluster", "Destination Cluster", 
                         "Source IP", "Destination IP", "Protocol", "Length (bytes)", "Flags (hex)"])

def start_monitoring():
    """Start capturing network packets."""
    setup_logging()
    print("📡 Starting network monitoring... Logging traffic in network_traffic_log.csv")
    
    # Capture only TCP/UDP packets
    sniff(prn=packet_callback, store=0, filter="tcp or udp")

if __name__ == "__main__":
    start_monitoring()
