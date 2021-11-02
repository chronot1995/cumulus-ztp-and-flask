#!/bin/bash
apt-get update -y
apt-get install curl -y
#curl -X POST http://<IP Address>:5000/Provision/`hostname -s`
curl -X POST http://10.10.140.11:5000/Provision/`hostname -s`
# CUMULUS-AUTOPROVISIONING