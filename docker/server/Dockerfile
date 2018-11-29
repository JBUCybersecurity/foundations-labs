FROM alpine:edge

MAINTAINER "Steve Helms" <SHelms@jbu.edu>

RUN apk --update add vsftpd supervisor nginx \
    && rm -rf /var/cache/apk/*

COPY supervisord.conf /etc/supervisord.conf

WORKDIR /data

CMD ["/usr/bin/supervisord","-c","/etc/supervisord.conf"]
