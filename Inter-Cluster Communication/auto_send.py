import subprocess
import random
import time

# Containers that can send messages
containers_a = [
    "container_1", "container_2", "container_3", "container_4", 
    "container_5", "container_6", "container_7"
]

containers_b = [
    "container_8", "container_9", "container_10", "container_11", 
    "container_12", "container_13", "container_14", "container_15", 
    "container_16"
]

# Possible message templates
messages = [
    "Hello from {sender} to Cluster {target}!",
    "Test message from {sender}.",
    "Network check from {sender} to {target}.",
    "Random packet data: {sender} -> {target}"
]

def send_random_message():
    """ Randomly selects a container and sends a message to a target cluster. """
    # Randomly choose whether to send from Cluster A or B
    if random.choice([True, False]):
        sender = random.choice(containers_a)
        target_cluster = "B"
    else:
        sender = random.choice(containers_b)
        target_cluster = "A"

    # Generate a random message
    message = random.choice(messages).format(sender=sender, target=target_cluster)

    # Execute the send_message.py script inside the chosen container
    cmd = f"docker exec {sender} python /send_message.py {target_cluster} \"{message}\""
    
    print(f"Executing: {cmd}")
    subprocess.run(cmd, shell=True)

if __name__ == "__main__":
    for i in range(5):
        send_random_message()
        time.sleep(random.randint(2, 8))  # Wait 2-8 seconds before sending another message
