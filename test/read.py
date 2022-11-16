import configparser

config = configparser.RawConfigParser()
config.read('config.properties')
#print(config.sections())
x=config.get('details', 'foo')
print(x)
