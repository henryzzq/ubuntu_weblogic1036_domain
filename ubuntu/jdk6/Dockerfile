FROM ubuntu:14.04

MAINTAINER Henry Zhao (https://www.linkedin.com/in/dreamerhenry)

ENV JAVA16_HOME /root/jdk/jdk1.6.0_45

USER root

RUN apt-get update && \
    apt-get install -y wget && \
    apt-get clean

#Download only script
RUN wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=0B-NEimEr29WddlFEbmhqTUVOZm8' -O gdown.pl

#Download JDK1.6
RUN perl gdown.pl 'https://docs.google.com/uc?export=download&id=0B-NEimEr29WddXo1X1hma0pTTXM' 'jdk-6u45-linux-x64.bin'

RUN mkdir /root/jdk

RUN chmod +x jdk-6u45-linux-x64.bin

RUN ./jdk-6u45-linux-x64.bin && \
    rm jdk-6u45-linux-x64.bin && \
    mv jdk1.6.0_45 /root/jdk


CMD ["bash"]