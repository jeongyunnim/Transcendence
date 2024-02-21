FROM python:3.12-alpine

RUN mkdir -p /var/www/django

ARG SSL_PATH=/etc/ssl/private
ARG DOMAIN=domain

WORKDIR /var/www/django

COPY ./tools/run_frontend.sh /home/run_frontend.sh

RUN chmod 755 /home/run_frontend.sh

RUN apk update && \
    apk --no-cache add \
    openssl \
    dumb-init

RUN pip install --upgrade pip \
    pip install django \
    django-environ \
    djangorestframework \
    djangorestframework-simplejwt \
    django-sslserver \
    django-filter \
    psycopg2-binary \
    poetry \
    django-extensions \
    drf-spectacular

RUN openssl genrsa -out ${SSL_PATH}/${DOMAIN}.key 2048 && \
    openssl req -new -key ${SSL_PATH}/${DOMAIN}.key -out ${SSL_PATH}/${DOMAIN}.crt \
    -subj "/C=KR/ST=Seoul/L=Gaepodong/O=42seoul/OU=Cadet/CN=${DOMAIN}" && \
    openssl x509 -req -days 1000 -in ${SSL_PATH}/${DOMAIN}.crt -signkey ${SSL_PATH}/${DOMAIN}.key -out ${SSL_PATH}/${DOMAIN}.crt

ENTRYPOINT ["dumb-init", "--", "/home/run_frontend.sh" ]