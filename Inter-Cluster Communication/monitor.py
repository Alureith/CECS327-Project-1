#!/usr/bin/env python
from scapy.all import sniff, IP, get_if_list
import time
import os

# Define the output file name for logging network traffic
OUTPUT_FILE = 'network_traffic_log.txt'

def initialize_log():
    """Initialize the log file with a header if it doesn't exist or is empty."""
    # Check if the file does not exist or is empty
    if not os.path.exists(OUTPUT_FILE) or os.path.getsize(OUTPUT_FILE) == 0:
        # Open the file in write mode and add the header
        with open(OUTPUT_FILE, mode='w') as file:
            file.write("Protocol Number | Time (s) | Source Cluster | Destination Cluster | Source IP | Destination IP | Protocol Name | Length (bytes) | Flags (hex)\n")
        print("Log file initialized.")

def log_packet(packet):
    """Process and log an IP packet to the text file."""
    # Ensure the packet has an IP layer
    if IP not in packet:
        return  # Only process IP packets

    # Capture the current time for the packet
    packet_time = time.time()
    # Extract source and destination IP addresses
    src_ip = packet[IP].src
    dst_ip = packet[IP].dst
    # Extract the protocol number from the IP header
    proto_num = packet[IP].proto
    # Get the full length of the packet
    length = len(packet)
    # Extract flags from the IP header in hexadecimal format
    flags = packet.sprintf('%IP.flags%')

    # Map protocol number to a human-readable string
    if proto_num == 6:
        protocol_name = "TCP"
    elif proto_num == 17:
        protocol_name = "UDP"
    elif proto_num == 1:
        protocol_name = "ICMP"
    else:
        protocol_name = "Other"

    # Identify clusters based on IP ranges
    if src_ip.startswith("2"):
        source_cluster = "A"
    elif src_ip.startswith("1"):
        source_cluster = "B"
    else:
        source_cluster = "Unknown"

    # Determine the destination cluster using similar logic
    if dst_ip.startswith("2"):
        destination_cluster = "A"
    elif dst_ip.startswith("1"):
        destination_cluster = "B"
    else:
        destination_cluster = "Unknown"

    # Format the log entry string with all the relevant details
    log_entry = f"{proto_num} | {packet_time:.2f} | {source_cluster} | {destination_cluster} | {src_ip} | {dst_ip} | {protocol_name} | {length} | {flags}\n"

    # Open the log file in append mode and write the log entry
    with open(OUTPUT_FILE, mode='a') as file:
        file.write(log_entry)
    
    # Print a debug message to the console
    print(f"Logged packet: {src_ip} -> {dst_ip} ({protocol_name})")

def sniff_traffic():
    """Start network traffic sniffing on all available interfaces."""
    print("Starting network traffic sniffing on all available interfaces...")
    # Retrieve a list of all network interfaces available on this system
    interfaces = get_if_list()
    print("Available interfaces:", interfaces)
    # Listen on all available interfaces at once
    sniff(iface=interfaces, prn=log_packet, store=0)

if __name__ == "__main__":
    # Initialize the log file with header if necessary
    initialize_log()
    # Begin capturing network traffic
    sniff_traffic()
