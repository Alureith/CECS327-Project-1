import csv
import time
import pyshark

LOG_FILE = './logs/network_traffic_log.csv'

# Define cluster IP ranges
CLUSTER_A_RANGE = "192.168.0."
CLUSTER_B_RANGE = "192.169.0."

# Define protocol mapping
PROTOCOL_MAP = {"TCP": 6, "UDP": 17}

def packet_callback(packet):
    """Callback function to process captured packets."""
    if 'IP' in packet:
        src_ip = packet.ip.src
        dst_ip = packet.ip.dst
        proto = packet.transport_layer
        length = len(packet)

        # Identify protocol
        protocol = proto if proto in PROTOCOL_MAP else "OTHER"

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
            comm_type = "Unknown"
            cluster_src = "Cluster A" if src_ip.startswith(CLUSTER_A_RANGE) else "Cluster B"
            cluster_dst = "Cluster B" if dst_ip.startswith(CLUSTER_B_RANGE) else "Cluster A"

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
            ""  # Placeholder for flags (no equivalent in PyShark for now)
        ]

        # Print captured packet info
        print(f"📡 {comm_type}: {src_ip} → {dst_ip} [{protocol}] Length: {length}")

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
    """Start capturing network packets using PyShark."""
    setup_logging()
    print("📡 Starting network monitoring... Logging traffic in network_traffic_log.csv")

    # Capture only TCP/UDP packets
    capture = pyshark.LiveCapture(interface='Wi-Fi', display_filter='tcp or udp', 
                                  tshark_path=r'C:\Program Files\Wireshark\tshark.exe')

    capture.apply_on_packets(packet_callback)

if __name__ == "__main__":
    start_monitoring()
