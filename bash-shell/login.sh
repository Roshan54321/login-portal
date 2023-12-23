#!/bin/bash

# Set the target URL
url="https://10.100.1.1:8090/login.xml"

# Set the username and password
username="076bct031"
password="kushal123"

# Set the data to be sent in the POST request
data="mode=191&username=$username&password=$password&a=1703265236405&producttype=0"

# Use curl to send the POST request

curl -k -X POST -d "$data" "$url"


