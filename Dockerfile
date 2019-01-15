FROM ubuntu:16.04

RUN apt-get clean && apt-get update && apt-get install -y locales
RUN apt-get install -y git
RUN apt-get install -y build-essential
RUN apt-get install -y python-dev
RUN apt-get install -y python-pip
RUN apt-get install -y libmysqlclient-dev
RUN python -m pip install "django<2"
RUN pip install Unipath==1.1
RUN pip install mysql-python

ADD . /source
WORKDIR /source