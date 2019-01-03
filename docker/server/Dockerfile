FROM alpine:edge

MAINTAINER "Steve Helms" <SHelms@jbu.edu>

RUN apk update && \
    apk upgrade && \
    apk --update add --no-cache vsftpd openssl supervisor nginx \
    bind-tools curl tcpdump shadow && \
    apk --update add --no-cache --virtual .build-dependencies \
    build-base curl linux-pam-dev openssl && \
    usermod -d /data/ftp vsftp

RUN \
    mkdir /build && \
    cd /build && \
    curl -sSL https://github.com/prapdm/libpam-pwdfile/archive/v1.0.tar.gz | tar xz --strip 1 && \
    make install && \
    cd / && \
    rm -rf /build && \
    apk del .build-dependencies && \
    rm -rf /var/cache/apk/* && \
    rm -rf /tmp/*

COPY vsftpd /etc/pam.d/
COPY supervisord.conf /etc/supervisord.conf

WORKDIR /data

CMD ["/usr/bin/supervisord","-c","/etc/supervisord.conf"]
