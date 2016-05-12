FROM ubuntu:14.04

MAINTAINER Henry Zhao (https://www.linkedin.com/in/dreamerhenry)

ENV JAVA16_HOME /root/jdk/jdk1.6.0_45

USER root

RUN mkdir /root/jdk

COPY jdk-6u45-linux-x64.bin /

RUN chmod +x jdk-6u45-linux-x64.bin

RUN ./jdk-6u45-linux-x64.bin && \
    rm jdk-6u45-linux-x64.bin && \
    mv jdk1.6.0_45 /root/jdk


CMD ["bash"]