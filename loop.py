#!/usr/bin/python3

import os
import sys
import time
import random
import requests
from ftplib import FTP

max_sleep = 30

def ftp():
    ftp = FTP(target_host)
    ftp.login()
    ftp.retrlines('LIST')
    ftp.quit()

def ping():
    response = os.system('ping -c 3 '+ target_host)

def sleepRand():
    time.sleep(random.randint(3,max_sleep))

def http():
    r = requests.get('http://'+ target_host)
    print(r.text)


# ----
# Main
# ----
if len(sys.argv) < 2:
    print("You must specify a server host to target.")
    sys.exit()

target_host = sys.argv[1]
available = [ftp,http,ping]

while True:
    # Sleep a random amount of time
    sleepRand()
    # Choose a random function to run
    random.choice(available)()
