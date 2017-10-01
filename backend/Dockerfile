FROM ubuntu:16.04

RUN apt-get update \
    && apt-get install -yq --no-install-recommends \
    openssh-server \
    python3 \
    python3-pip \
    && pip3 install --upgrade pip \
    && pip3 install setuptools \
    && pip3 install watchdog

RUN mkdir /var/run/sshd

# set password of root
RUN echo 'root:screencast' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

# for ssh to use python executable in IDE
EXPOSE 22

# for flask web server
EXPOSE 8081

ADD . /app
WORKDIR /app

# This is the runtime command
CMD ./install.sh \
    && service ssh restart \
    && (python3 watcher.py &) \
    && python3 app.py


