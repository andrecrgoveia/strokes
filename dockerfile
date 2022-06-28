FROM ubuntu:20.04

WORKDIR /python-docker

ENV TZ=Europe/Minsk
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update \
 && apt-get install -y sudo

RUN adduser --disabled-password --gecos '' docker
RUN adduser docker sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER docker

RUN sudo apt-get install xz-utils -y

RUN sudo apt-get install wget -y

RUN sudo wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

RUN sudo apt-get install ./google-chrome-stable_current_amd64.deb -y


RUN sudo apt-get install python3.8 -y

RUN sudo apt-get install python3-pip -y

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5001

CMD ["python3","apiaccsflask.py"]
