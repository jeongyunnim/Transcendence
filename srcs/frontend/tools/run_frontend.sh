#!/bin/sh

python manage.py makemigrations

python manage.py migrate

# todo ssl 가장 나중에 하자. 그리고 오류 생김. sslserver 구동할 수 있게 패키지 받아야 함. django settings에 INSTALLED_APP에도 설정 해야 함.
# python manage.py runsslserver --certificate /etc/ssl/private/domain.crt --key /etc/ssl/private/domain.key 0:8000
python manage.py runserver 0:8000