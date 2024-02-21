#!/bin/sh



python manage.py makemigrations

python manage.py migrate

# python manage.py runsslserver --certificate /etc/ssl/private/domain.crt --key /etc/ssl/private/domain.key 0:8000
python manage.py runserver 0:8000