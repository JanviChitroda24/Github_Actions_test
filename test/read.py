import configparser

config = configparser.RawConfigParser()
config.read('config.properties')
print(config.sections())
#x=config.get('details', 'foo')
#print(x)

"""
FROM python:latest


#Labels as key value pair
LABEL Maintainer="roushan.me17"


# Any working directory can be chosen as per choice like '/' or '/home' etc
# i have chosen /usr/app/src
WORKDIR /usr/app/src

#to COPY the remote file at working directory in container
COPY read.py ./
# Now the structure looks like this '/usr/app/src/test.py'


#CMD instruction should be used to run the software
#contained by your image, along with any arguments.

CMD [ "python", "./test/read.py"]


"""