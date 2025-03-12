# CECS327

# Project 1: A bite of Distributed Communication

# Overview 

This project demonstrates how distributed communication works by designing and implementing
a small scale distributed system using Docker. This is done by  developing and analyzing
communication protocols to optimize message delivery across nodes in a simulated network. 


## ** Project Files **

- "Inter-cluster communication" which contains: 
    - cluster master.py
    - docker-compose.yml
    - send_message.py
    - auto_send.py
    - monitor.py
    - Dockerfile
    - network_traffic_log.txt

- broadcast reciever.py
- broadcast_sender.py
- docker-compose.yml
- multicast_reciever.py
- multicast_sender.py
- README.md

## **Installation Instructions **

### **Step 1: Install Docker**

Ensure that Docker is installed on your system. You can download it from:

- [Docker for Windows/macOS](https://www.docker.com/products/docker-desktop)
- [Docker for Linux](https://docs.docker.com/engine/install/)

Verify the installation:

```bash
docker --version
docker run hello-world
```

---

## **Compiling and Running the Application**

### **Step 2: Running Multicast and Broadcast**

Open up powershell and navigate to the project directory and run the following commands: 

```
docker-compose up
```

This commands starts all 16 containers and runs the python scripts inside the docker-compose.yml file.

Once the containers have started up, you will see print statements of the containers communicating with
each other and the containers will automatically exit once done. 

To close the containers once they succesffully exit after commuincating, type the following command:

```
docker-compose down
```

### **Step 3: Inter-Cluster Communication **

From the previous steps, navigate to the folder "Inter-cluster communication". Run the following command to start the containers in "detached" mode which opens them in the background:

``` 
docker-compose up --build -d
```

To build the containers. Once the containers have been built, to send a message from Cluster A to Cluster B, type the following command:

```
docker exec -it container_1 python send_message.py B "Hello from Cluster A!"
```
This sends a message from container 1 to Cluster B.

To view the steps the message goes through to reach its final destination type in the command:

```
docker logs cluster_master_a
```

To send a message from Cluster B to Cluster A enter the command:

```
docker exec -it container_8 python send_message.py A "Hello from Cluster B!"
```

Or the user can use the script "auto_message.py" using the command

```
python auto_message.py
```

And to view the logs of this process enter the command

```
docker logs cluster_master_b
```

### **Step 4: Monitering Commuincations **

So start up a moniter using scapy, once the containers are running using detached mode, enter the following command:

```
python monitor.py
```

that should start a log of communications between the cluster and store the infomration within the "network_traffic_log.py" file.