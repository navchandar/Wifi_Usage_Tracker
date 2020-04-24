import fast
import requests
import time
import subprocess
import sys
import urllib3
urllib3.disable_warnings()

gurl='https://docs.google.com/forms/d/e/******/formResponse'
gFormPreFilledURL = 'https://docs.google.com/forms/d/*********'

speed = None
# since we dont want to track work wifi
WifiName = "Your Home Wifi Name"

try:
    p = subprocess.check_output( ["powershell.exe", "netsh", "wlan", "show", "interfaces"],  shell=True)
    content = p.decode()
    if WifiName in content:
        print (f"Connected to Wifi : {WifiName}")
        speed = fast.main()
        print(f"Speed = {speed}")
except Exception as e:
    print(e)


if speed:
    gFormParams = {'entry.198552954' : time.strftime('%d/%m/%Y %R'), 'entry.4356128' : speed}
    resp = requests.post(gurl, data=gFormParams, verify=False)
    if resp.status_code == 200:
        print('Successfully posted data to Form.')
    else:
        print('Error: %s' % resp.content)

