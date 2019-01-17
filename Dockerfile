FROM ubuntu:16.04

# Logs locations
RUN mkdir /logs
RUN mkdir /logs/supervisor

RUN apt-get clean && apt-get update && apt-get install -y locales
RUN apt-get install -y git
RUN apt-get install -y build-essential
RUN apt-get install -y python-dev
RUN apt-get install -y python-pip
RUN apt-get install -y libmysqlclient-dev
RUN apt-get install -y supervisor

# ES Locale
RUN locale-gen es_ES.UTF-8
ENV LANG es_ES.UTF-8
ENV LC_ALL es_ES.UTF-8

ADD . /source
WORKDIR /source

RUN pip install -r requirements.txt


COPY /supervisord.conf /etc/supervisor/conf.d/supervisord.conf
CMD ["/usr/bin/supervisord"]