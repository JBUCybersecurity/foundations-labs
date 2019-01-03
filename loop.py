#!/usr/bin/python3

import os
import sys
import time
import random
import requests
from requests.auth import HTTPBasicAuth
from ftplib import FTP

max_sleep = 30
sites = ['google.com','yahoo.com','ford.com','tesla.com','nissandriven.com']
ftp_user = "neo"
ftp_pass = "thematrixhasyou"
http_user = "admin"
http_pass = "thematrixhasyou"

def ftp():
    if random.randint(1,10) % 2 == 0:
        try:
            ftp = FTP(target_host,ftp_user,ftp_pass)
        except:
            ftp = FTP(target_host)
    else:
        ftp = FTP(target_host)
    ftp.login()
    ftp.retrlines('LIST')
    ftp.quit()

def ping():
    response = os.system('ping -c 3 '+ target_host)

def dig():
    fqdn = random.choice(sites)
    response = os.system('dig '+ fqdn)

def sleepRand():
    time.sleep(random.randint(3,max_sleep))

def http():
    r = requests.get('http://'+ target_host)
    print(r.text)

def http_auth():
    r = requests.get('http://'+ target_host+'/secure/',
            auth=(http_user,http_pass))
    print(r.text)


# ----
# Main
# ----
if len(sys.argv) < 2:
    print("You must specify a server host to target.")
    sys.exit()

target_host = sys.argv[1]
available = [dig,ftp,http,ping,http_auth]

while True:
    # Sleep a random amount of time
    sleepRand()
    # Choose a random function to run
    random.choice(available)()
