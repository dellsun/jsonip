FROM centos:7

RUN yum -y update
RUN yum -y install epel-release
RUN yum -y install python-pip
RUN pip install Django==1.11.15

ADD jsonip/ /opt/jsonip/

ENV TZ Asia/Shanghai
EXPOSE 9999
WORKDIR /opt/jsonip/

ENTRYPOINT python manage.py runserver 0.0.0.0:9999