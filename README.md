# cumulus-ztp-and-flask

### Description

This demo will automagically configure Cumulus Linux 4.4 and below via ZTP + Ansible from a Python3 Flask server

Thanks to Jason Heller for putting the Python2 version of this application together, as it was a beyond valuable reference.

### Instructions

1. Validate that a ZTP server for Cumulus Linux is running on the network

2. Pull down this git repo with the following command:

```
git clone https://gitlab.com/nvidia-networking/systems-engineering/poc-support/cumulus-ztp-and-flask
```

3. Change directories with the following command:

```
cd cumulus-ztp-and-flash
```

4. The included file, "ztp-flask.sh," is an example of the "ztp.sh" file that we will use in this demo. Your ZTP server should be updated accordingly. This file will tell the Cumulus switch to http to this demo server and pull down the proper configuration.

5. Edit the Ansible "hosts" file found in the "docker" directory with the MAC address of the switch in question. Here's an example of that file:

```
[switches]
98039BC0EDC4 ansible_host=192.168.255.101
```

Second, the host file contains the credentials to SSH into the Cumulus switch. Change these values appropriately.

The "ansible_host" is the OOB IP address that will be handed out via DHCP and the first string is the MAC Address in all caps.

6. Next, we will make some changes to the underlying Ansible configuration to provision the switch correctly. First, under the docker/group_vars/all.yaml file, you find the test configuration that we are using. For demo purposes, change the key under "node" from "98039BC0EDC4" to the MAC address of your system.

7. The Ansible configuration is stored under the following directory docker/roles/switches. This demo will configure FRR, the interfaces file, and the hostname to the value stored in the all.yaml file from step 6.

8. OPTIONAL: This demo was tested on an Ubuntu 20.04 server running Docker. The following commands install Docker (skip if Docker is already installed on your machine)"

```
sudo apt-get install software-properties-common
sudo apt-key adv --fetch-keys https://download.docker.com/linux/ubuntu/gpg
sudo apt-get install -y docker-ce docker-compose
```

9. Change directories with the following command:

```
cd docker
```

10. Pull down and build the docker container for this demo:

```
sudo docker build -t python-docker:latest .
```

The output for the above command will look like the following:

```
Sending build context to Docker daemon  20.48kB
Step 1/12 : FROM python:3.9-slim-buster
3.9-slim-buster: Pulling from library/python
b380bbd43752: Pull complete
14063a2781d6: Pull complete
5a63271f8164: Pull complete
8bcf4fd3160a: Pull complete
537014b02327: Pull complete
Digest: sha256:76eaa9e5bd357d6983a88ddc9c4545ef4ad64c50f84f081ba952c7ed08e3bdd6
Status: Downloaded newer image for python:3.9-slim-buster
 ---> 564b1a543bd3
Step 2/12 : WORKDIR /app
 ---> Running in 7d97ceeefd33
Removing intermediate container 7d97ceeefd33
 ---> c2f5b77098e2
Step 3/12 : COPY requirements.txt requirements.txt
 ---> 6caa3386cee8
Step 4/12 : RUN pip3 install -r requirements.txt
 ---> Running in 91b203f7cb1b
Collecting click==8.0.1
  Downloading click-8.0.1-py3-none-any.whl (97 kB)
Collecting Flask==2.0.1
  Downloading Flask-2.0.1-py3-none-any.whl (94 kB)
Collecting itsdangerous==2.0.1
...
```

11. Run the Docker container with the following command:

```
sudo docker run --name ztpflask3 --publish 5000:5000 python-docker
```

The output for the above command will look like the following:

```
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://172.17.0.2:5000/ (Press CTRL+C to quit)
 ...
```

12. At this point, you can run through the entire ZTP process with the Cumulus switch, if you would like. Something else you can do is to run the following command to connect with Flask and to start the Ansible provisioning of the Cumulus switch:

```
curl -X POST http://ubuntu:5000/Provision/98039BC0EDC4
```

In the above, the hostname / IP address would point to the server running this demo.

You will see the following output on the demo server when the Ansible process begins:

```
 * Running on http://172.17.0.2:5000/ (Press CTRL+C to quit)

PLAY [switches] ****************************************************************

TASK [switches : Update Hostname] **********************************************
...
```

There will be a new Cumulus configuration on the switch after the Ansible playbook is complete.

### Troubleshooting

1. Reset the ZTP test by deleting and removing the Docker image:

```
sudo docker system prune -a
```

2. Go back up to step "11" and restart the ZTP demo

### Helpful Docker Commands

```
sudo docker system prune -a
sudo docker exec -it <container name> /bin/bash
sudo docker ps
sudo docker container stats
sudo docker image ls
sudo docker image rm <container ID>
```
