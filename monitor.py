import pyshark
import csv
import time

# Define the interface you want to capture on
INTERFACE = "eth0"  # Change this to match the correct network interface in your container
LOG_FILE = "/app/logs/network_traffic_log.csv"

def parse_packet(packet):
    try:
        timestamp = float(packet.sniff_time.timestamp())  # Packet capture timestamp
        src_ip = packet.ip.src
        dst_ip = packet.ip.dst
        protocol = packet.transport_layer  # TCP/UDP
        length = packet.length
        flags = getattr(packet.tcp, "flags", "N/A") if "TCP" in protocol else "N/A"
        
        # Determine if it's intra-cluster or inter-cluster
        if src_ip.startswith("192.168.0.") and dst_ip.startswith("192.168.0."):
            type_comm = "Intra-Cluster"
        elif src_ip.startswith("192.169.0.") and dst_ip.startswith("192.169.0."):
            type_comm = "Intra-Cluster"
        else:
            type_comm = "Inter-Cluster"

        # Determine message type based on IPs (Broadcast/Multicast/Anycast)
        if dst_ip.endswith(".255"):  # Broadcast
            msg_type = "Broadcast"
        elif dst_ip.startswith("224.") or dst_ip.startswith("239."):  # Multicast
            msg_type = "Multicast"
        else:
            msg_type = "Anycast"

        return [type_comm, f"{timestamp:.6f}", src_ip, dst_ip, protocol, length, flags, msg_type]

    except AttributeError:
        return None

def capture_traffic():
    print(f"Starting network capture on {INTERFACE}...")
    with open(LOG_FILE, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Type", "Time (s)", "Source IP", "Destination IP", "Protocol", "Length (bytes)", "Flags (hex)", "Message Type"])
        
        capture = pyshark.LiveCapture(interface=INTERFACE)
        for packet in capture.sniff_continuously():
            parsed_data = parse_packet(packet)
            if parsed_data:
                csv_writer.writerow(parsed_data)
                print(parsed_data)

if __name__ == "__main__":
    capture_traffic()
