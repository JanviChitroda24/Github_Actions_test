

import os
arr=[]
with open('config.properties', "r") as file:
    data = file.readlines()
    for line in data:
        arr.append(line.split("=", 1))
print(arr)
with open(os.environ['GITHUB_OUTPUT'],'a') as fh:
    for val in enumerate(arr):
        val2=str(val[1])
        val2=val2.rstrip('\n')
        print(f'{val[0]}={val2}',file=fh)



"""
import configparser

config = configparser.RawConfigParser()
config.read('config.properties')
print(config.sections())
appName=config.get('details', 'appName')
healthCheck=config.get('details', 'healthCheck')
print(appName,healthCheck)
"""