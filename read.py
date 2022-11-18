
"""
import os

with open('config.properties', "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split("=", 1)
        print(word)

foo=bar
appname=zmgo-agjewk
eskj=ekfl/dmsekf/fsmke/sdf=dckjsvnkew

"""
import configparser

config = configparser.RawConfigParser()
config.read('config.properties')
print(config.sections())
x=config.get('details', 'foo')
print(x)
