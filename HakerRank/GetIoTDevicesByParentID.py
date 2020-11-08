#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'avgRotorSpeed' function below.
#
# URL for cut and paste
# https://jsonmock.hackerrank.com/api/iot_devices/search?status={statusQuery}&page={number}
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING statusQuery
#  2. INTEGER parentId
#

import requests
def avgRotorSpeed(statusQuery, parentId):
    # Write your code here
      
    URL = f'https://jsonmock.hackerrank.com/api/iot_devices/search?status={statusQuery}&page=0'
    r = requests.get(url = URL)
    data = r.json()
    total_P = math.ceil(data['total'] / data['per_page'])
    totalRotorSpeed = 0
    counter = 0
    
    for i in range(total_P + 1):
        URLloop = f'https://jsonmock.hackerrank.com/api/iot_devices/search?status={statusQuery}&page={i}'
        req = requests.get(url = URLloop)
        dataLoop = req.json()
        for device in dataLoop['data']:
            # print(device)
            if 'parent' in device.keys() and device['parent'] is not None and device['parent']['id'] == parentId:
                totalRotorSpeed += device['operatingParams']['rotorSpeed']
                counter += 1
                
    if counter == 0:
        return 0
    
    return totalRotorSpeed // counter
    
#2 cases missed... dont know

if __name__ == '__main__':