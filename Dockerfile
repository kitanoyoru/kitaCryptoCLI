FROM ubuntu:latest

LABEL name="kitacrypto"

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN apt update && apt install python3-pip git -y && pip3 install --no-cache-dir pipenv

WORKDIR /kitacrypto

ADD Pipfile Pipfile.lock .
RUN /bin/bash -c "pip3 install --no-cache-dir -r <(pipenv lock -r)"

ADD . /kitacrypto
RUN pip3 install --no-cache-dir /kitacrypto

EXPOSE 3000

