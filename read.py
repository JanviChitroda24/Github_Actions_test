

import os
arr=[]
with open('config.properties', "r") as file:
    data = file.readlines()
    for line in data:
        arr.append(line.split("=", 1))
print(arr)
with open(os.environ['GITHUB_OUTPUT'],'a') as fh:
    for val in enumerate(arr):
        print(val[0])
        val2=str(val[1])
        print(val2)
        temp=val2.rstrip('\n')
        print(temp)
        print(f'{val[0]}={temp}',file=fh)



"""
import configparser

config = configparser.RawConfigParser()
config.read('config.properties')
print(config.sections())
appName=config.get('details', 'appName')
healthCheck=config.get('details', 'healthCheck')
print(appName,healthCheck)
"""