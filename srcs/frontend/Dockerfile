FROM python:3.12-alpine

RUN mkdir -p /var/www/django

WORKDIR /var/www/django

RUN pip install --upgrade pip \
    pip install django \
    django-environ \
    djangorestframework \
    django-filter \
    psycopg2-binary

COPY ./tools/srcs /var/www/django/

CMD [ "python", "/var/www/django/manage.py", "runserver", "0.0.0.0:8000" ]