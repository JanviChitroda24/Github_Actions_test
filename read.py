

import os
arr=[]
with open('config.properties', "r") as file:
    data = file.readlines()
    for line in data:
        arr.append(line.split("=", 1))
print(arr)
with open(os.environ['GITHUB_OUTPUT'],'a') as fh:
    for val in enumerate(arr):
        print(f'{val[0]}={val[1].strip()}',file=fh)



"""
import configparser

config = configparser.RawConfigParser()
config.read('config.properties')
print(config.sections())
appName=config.get('details', 'appName')
healthCheck=config.get('details', 'healthCheck')
print(appName,healthCheck)
"""