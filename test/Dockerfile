FROM ubuntu:latest

RUN apt update
RUN apt install python3 -y

WORKDIR /usr/appc/src

COPY ready.py ./

CMD ["python3", "./read.py"]