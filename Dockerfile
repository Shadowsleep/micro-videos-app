FROM python:3.10.2-slim

RUN apt update && apt install -y --no-install-recommends default-jre

#por motivo de segurança é bom criar um user ae nao trabalhar com o root
#RUN useradd -ms /bin/bash python

RUN pip install pdm

#usar o user criado
#USER python

#especifica o caminho q vai ficar a aplicação no container
WORKDIR /home/python/app

#config do python path (estudar o que é isso)
ENV PYTHONPATH=${PYTHONPATH}/home/python/app/src
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64

CMD [ "tail","-f","/dev/null" ]