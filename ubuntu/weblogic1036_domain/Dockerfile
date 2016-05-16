FROM zhiqzhao/ubuntu_weblogic103:latest

MAINTAINER Henry Zhao (https://www.linkedin.com/in/dreamerhenry)

USER root

ENV CONFIG_JVM_ARGS '-Djava.security.egd=file:/dev/./urandom'

#Download create domain script
RUN wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=0B-NEimEr29WdQThnYjVnRmUwd2c' -O create-wls-domain.py

RUN mv create-wls-domain.py /root/Oracle && \
    chmod +x /root/Oracle/create-wls-domain.py

WORKDIR /root/Oracle/Middleware

RUN /root/Oracle/Middleware/wlserver_10.3/common/bin/wlst.sh -skipWLSModuleScanning /root/Oracle/create-wls-domain.py

# Expose Node Manager default port, and also default http/https ports for admin console
EXPOSE 7001 5556 

ENV PATH $PATH:/root/Oracle/Middleware/wlserver_10.3/common/bin:/root/Oracle/Middleware/user_projects/domains/base_domain/bin

CMD ["startWebLogic.sh"]