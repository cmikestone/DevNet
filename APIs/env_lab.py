#! /usr/bin/env python3

#User Input
#Select the lab env that you will be using
#sandbox - DevNet Always on / Reserved sandboxes
#express - DevNet Express lab backend
#custom - Your own custom lab service
#This is a direct copy from Cisco

ENVIRONMENT_IN_USE = "sandbox"

#Set the Env Vars based on lab Env in use
if ENVIRONMENT_IN_USE == "sandbox":
    dnac = {
        "host": "sandboxdnac.cisco.com",
        "port": 443,
        "username": "devnetuser",
        "password": ""
    }
