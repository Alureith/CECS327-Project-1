from scapy.all import *
import csv
import time

# Define the CSV file to store the log data
OUTPUT_FILE = 'network_traffic_log.csv'

# Function to process and log the packet
def log_packet(packet):
    # Extract packet details
    packet_time = time.time()  # Time in seconds when the packet was captured
    src_ip = packet[IP].src if IP in packet else None
    dest_ip = packet[IP].dst if IP in packet else None
    protocol = packet.proto if IP in packet else None
    length = len(packet)
    flags = packet.sprintf('%IP.flags%')  # Flags in hexadecimal
    
    # Map the protocol to a string
    protocol_str = ""
    if protocol == 6:
        protocol_str = "TCP"
    elif protocol == 17:
        protocol_str = "UDP"
    elif protocol == 1:
        protocol_str = "ICMP"
    else:
        protocol_str = "Unknown"
    
    # Identify which cluster the packet belongs to
    if src_ip and dest_ip:
        if src_ip.startswith("192.168.0"):
            source_cluster = "Cluster A"
        elif src_ip.startswith("192.169.0"):
            source_cluster = "Cluster B"
        else:
            source_cluster = "Unknown Cluster"
        
        if dest_ip.startswith("192.168.0"):
            destination_cluster = "Cluster A"
        elif dest_ip.startswith("192.169.0"):
            destination_cluster = "Cluster B"
        else:
            destination_cluster = "Unknown Cluster"
        
        # Log the packet to CSV file
        with open(OUTPUT_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                protocol_str, packet_time, source_cluster, destination_cluster,
                src_ip, dest_ip, protocol_str, length, flags
            ])
        print(f"Logged packet: {src_ip} -> {dest_ip} ({protocol_str})")

# Function to start sniffing the network
def sniff_traffic():
    print("Starting network traffic sniffing...")
    
    # Start sniffing on all interfaces (you can specify a particular interface if needed)
    sniff(prn=log_packet, store=0)

if __name__ == "__main__":
    # Create or initialize CSV file with headers
    with open(OUTPUT_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            "Type", "Time (s)", "Source Cluster", "Destination Cluster",
            "Source IP", "Destination IP", "Protocol", "Length (bytes)", "Flags (hex)"
        ])
    
    # Start sniffing traffic
    sniff_traffic()
