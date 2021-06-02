#! /usr/bin/env python3

from env_lab import dnac
import json
import requests
import urllib3
from requests.auth import HTTPBasicAuth
from prettytable import PrettyTable

#Create the Table and Columns with Pretty Tables
dnac_devices = PrettyTable(['\033[1mHostname','Platform Id','Software Type','Software Version','Up Time\033[0m' ])
dnac_devices.padding_width = 1

#Silence the insecure warning due to SSL Cert Messaging
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#define headers as JSON because we're going to be requesting the GET to come back as JSON
headers = {
                'content-type': "application/json",
                'x-auth-token': ""  #We will be filling this value in later after we authenticate, this is the begining of our dictionary defs
}

#Here the function logs in with the data from env_lab, we construct our URL from env_lab too, 
#this line is also where we get the Token. In the Return response.json(), the body that comes back after
#the POST will have a Token that is provided as part of the response. We will store it and use it later

def dnac_login(host, username, password):
    url = f"https://{host}/api/system/v1/auth/token"
    response = requests.request("POST", url, auth=HTTPBasicAuth(username, password), headers=headers, verify=False)
    return response.json()["Token"]

#Here the function uses the dnac values from env_lab, and also the token that we just stored. The URL is set
#to where we can get the data using the dnac values, then the Headers key from above, x-auth-token, now has the
#value of Token from the previous function applied as its value. Then we use a requests.get to pull the values. 
#We then send it to a varaible called data, where we take the data from response and run it through the .json
#module, i.e. response.json. We then iterate through what's now stored in what's coming back to data adding each as 
#a new row "add" by the values previously defined, i.e. dnac_devices.add_row([item["hostname"], item["platformId"]])

def network_device_list(dnac, token):
    url = f"https://{(dnac['host'])}/api/v1/network-device"
    headers["x-auth-token"] = token
    response = requests.get(url, headers=headers, verify=False)
    data = response.json()
    for item in data['response']:
        dnac_devices.add_row([item["hostname"],item["platformId"],item["softwareType"],item["softwareVersion"],item["upTime"] ])

#Run the functions: dnac_login - pass the values from env_lab
#network_device_list - pass dnac values for auth and new token from dnac_login and build the table

login = dnac_login(dnac["host"], dnac["username"], dnac["password"])
network_device_list(dnac, login)

#Print the output from dnac_devices that has been built with dnac_login and network_device_list
print(dnac_devices)
    