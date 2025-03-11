FROM python:3.9

# Install required dependencies
RUN pip install pyshark

# Install scapy and tshark (Wireshark)
RUN apt-get update && apt-get install -y tshark && apt-get clean

# Set the working directory
WORKDIR /app

# Copy the monitoring script into the container
COPY monitor.py /app/monitor.py

# Run the monitoring script
CMD ["python", "monitor.py"]