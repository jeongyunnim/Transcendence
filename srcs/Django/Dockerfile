FROM python:3.12-alpine

RUN mkdir -p /var/www/django

WORKDIR /var/www/django

RUN pip install --upgrade pip &&\
    pip install django

# CMD [ "python", "/var/www/django/jeseo_site/manage.py", "runserver", "0.0.0.0:8000" ]