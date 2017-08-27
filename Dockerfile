# Get amazonlinux:latest
FROM amazonlinux:latest

EXPOSE 80

# Set timezone
RUN cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

# Install libraries
RUN yum -y update && \
    yum -y install wget && \
    yum -y install tar && \
    yum -y install gcc* && \
    yum -y install openssl-devel && \
    yum -y install git && \
    yum -y install sqlite-devel && \
    yum -y install vi

RUN touch /etc/sysconfig/i18n && \
    echo "LANG=\"ja_JP.UTF-8\"" > /etc/sysconfig/i18n && \
    source /etc/sysconfig/i18n && \
    export LANG

# Install Python3
ENV PYTHON_VERSION 3.6.2
RUN cd /usr/local/src && \
    wget https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz && \
    tar xzvf Python-${PYTHON_VERSION}.tgz && \
    cd Python-${PYTHON_VERSION} && \
    ./configure && \
    make && \
    make install

# Install nginx, Circus, chaussette
RUN rpm -ivh http://nginx.org/packages/centos/6/noarch/RPMS/nginx-release-centos-6-0.el6.ngx.noarch.rpm && \
    yum -y install nginx && \
    chkconfig nginx --level 3 on && \
    pip3 install circus && \
    pip3 install chaussette

# Install test tool
#RUN yum install npm && \
#    pip3 install selenium && \
#    npm install -g phantomjs

# Set init
RUN touch /etc/sysconfig/network && \
    mkdir /var/log/dandelion
ENV PYTHONDONTWRITEBYTECODE 1
ENV DOCKER true

# copy project
WORKDIR /project
ADD . /project

RUN pip3 install --no-cache-dir -r requirements.txt
VOLUME ["/project"]
