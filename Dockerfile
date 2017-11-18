FROM centos:7

RUN yum update -y && yum install -y \
	https://centos7.iuscommunity.org/ius-release.rpm

RUN yum install -y \
	python36u \
	python36u-devel \
	python36u-pip \
	&& pip3.6 install awscli

RUN mkdir app

WORKDIR /app

ADD . .

RUN pip3.6 install -r requirements.txt

RUN pip3.6 install .

ENTRYPOINT ["prestige"]
CMD ["--help"]	