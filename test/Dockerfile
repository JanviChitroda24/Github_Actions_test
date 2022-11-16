

FROM python:latest
COPY read.py /usr/bin/
RUN apk add --no-cache bash
RUN ln -s /usr/bin/read.py
ENTRYPOINT ["read.py"]