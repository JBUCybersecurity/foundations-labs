FROM alpine:edge

MAINTAINER "Steve Helms" <SHelms@jbu.edu>

RUN apk --update add python3 supervisor \
    && pip3 install --upgrade pip requests \
    && rm -rf /var/cache/apk/*

COPY supervisord.conf /etc/supervisord.conf

WORKDIR /data

CMD ["/usr/bin/supervisord","-c","/etc/supervisord.conf"]
