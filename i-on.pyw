import ast
import time
import random
import requests
from bs4 import BeautifulSoup

username = 'UserName'
password = 'PassPhrase'
link = 'https://customer.i-on.in/dataUsageHistory?user=' + username + '&crmType=hcrm'
gurl='https://docs.google.com/forms/d/e/******/formResponse'
gFormPreFilledURL = 'https://docs.google.com/forms/d/*********'


session = requests.Session()
header = { 'Accept': '*/*',
           'Accept-Encoding': 'gzip, deflate, br',
           'Connection': 'keep-alive',
           'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
           'Host': 'customer.i-on.in',
           'Origin': 'https://customer.i-on.in',
           'Referer': 'https://customer.i-on.in/',
           'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4; Nexus 5 Build/_BuildID_) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36',
           'X-Requested-With': 'XMLHttpRequest'}

resp = session.get('https://customer.i-on.in', verify=False)
time.sleep(random.randint(1, 3))
resp = session.post('https://customer.i-on.in/findCRM',  headers=header, data=('crm=hcrm&user=' + username +'&password='+ password), verify=False)
time.sleep(random.randint(1, 3))
response = session.get(link, verify=False)
time.sleep(random.randint(1, 3))
session.close
 
content = (response.content).decode(""utf-8"")
dictContent = ast.literal_eval(content)

if dictContent['guidance']['message'] == 'success':
    UsedDataMB = dictContent['Details']['UsedDataMB']
    UsedTimeMIN = dictContent['Details']['UsedTimeMIN']
    RemainDataMB = dictContent['Details']['RemainDataMB']
    RemainTimeMIN = dictContent['Details']['RemainTimeMIN']
    
    # print(time.strftime('%d/%m/%Y'), UsedDataMB, UsedTimeMIN, RemainDataMB, RemainTimeMIN)
    gFormParams = {'entry.1682821377' : time.strftime('%d/%m/%Y'), 'entry.749538580' : UsedDataMB,
                   'entry.1147404457' : UsedTimeMIN, 'entry.1287839677' : RemainDataMB, 'entry.748571465' : RemainTimeMIN }

    resp = requests.post(gurl, data=gFormParams, verify=False)
    if resp.status_code == 200:
        print('Successfully posted data to Form.')
    else:
        print('Error: %s' % resp.content)

else:
    print(content)
