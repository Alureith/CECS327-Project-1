# Use the official Python image as a base
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the necessary scripts into the container
COPY ./monitor.py /app/monitor.py
COPY ./send_message.py /app/send_message.py
COPY ./auto_send.py /app/auto_send.py

# Install the required Python packages
RUN pip install scapy

# Set the default command to run your monitoring script
CMD ["python", "monitor.py"]