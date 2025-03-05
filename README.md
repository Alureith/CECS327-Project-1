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

### **Step 3:  **

