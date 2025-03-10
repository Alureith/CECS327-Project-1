FROM python:3.9

# Install required dependencies
RUN apt-get update && apt-get install -y tcpdump libpcap-dev

# Set the working directory
WORKDIR /app

RUN pip install --no-cache-dir scapy

# Copy the monitoring script into the container
COPY network_monitor.py /app/network_monitor.py

# Run the network monitoring script
CMD ["python", "network_monitor.py"]
