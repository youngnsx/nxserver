FROM ubuntu:16.04

# RUN echo "Asia/Taipei" > /etc/timezone

RUN apt-get update \
    && apt-get install -y apt-utils \
    wget \
    python \
    cron \
    iputils-ping \
    systemd-sysv \
    psmisc \
    libsm6 libice6 libaudio2 libogg0 libxfixes3 libxrender1 libfontconfig1 libgl1-mesa-glx libglib2.0-0 \
    cifs-utils \
    syslinux \
    net-tools \
    dmidecode \
    # tzdata \
    && rm -rf /var/lib/apt/lists/*

# RUN dpkg-reconfigure -f noninteractive tzdata

# wget http://updates.networkoptix.com/default_cn/28738/linux/nxwitness_cn-server-3.2.0.28738-linux64.deb 

ADD ./networkoptix /opt/networkoptix
WORKDIR /opt/networkoptix

CMD ["/opt/networkoptix/mediaserver/bin/mediaserver-bin", "-e"]

# PORT
EXPOSE 7001