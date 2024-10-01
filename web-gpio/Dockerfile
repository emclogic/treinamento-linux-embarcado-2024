FROM debian:bookworm

ENV WORK=/project

ENV TZ=Etc/UTC
ENV LANG=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8

EXPOSE 5000/tcp

ARG DEBIAN_FRONTEND=noninteractive

RUN \
    apt-get update && apt-get -y install --no-install-recommends \
    sudo tzdata locales python3 python3-pip python3-dev \
    libgpiod-dev python3-libgpiod python3-flask python3-flaskext.wtf \
    && apt-get clean

RUN \
    ln -fs /usr/share/zoneinfo/Etc/UTC /etc/localtime && \
    echo ${TZ} > /etc/timezone && \
    dpkg-reconfigure -f noninteractive tzdata && \
    locale-gen ${LC_ALL}

RUN groupadd gpio

RUN usermod -aG gpio root
    
RUN echo "root:rootpass" > /root/passwdfile
RUN chpasswd -c SHA512 < /root/passwdfile && \
    rm /root/passwdfile

WORKDIR ${WORK}

COPY app.py ${WORK}/app.py
COPY templates ${WORK}/templates

CMD ["python3", "app.py"]
