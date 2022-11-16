import configparser

config = configparser.RawConfigParser()
x=config.get(config.sections()[0], 'foo')
print(x)
