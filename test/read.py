import configparser

config = configparser.RawConfigParser()
config.read('config.properties')
x=config.get(config.sections()[0], 'foo')
print(x)
