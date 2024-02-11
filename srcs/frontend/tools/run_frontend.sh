#!/bin/sh

if [ ! -d "~/.pg_service.conf" ]; then
    cat << EOF > .pg_service.conf
[mydb]
host=${FE_DB}
dbname=${FE_DB}
port=${FE_DB_PORT}
user=${FE_DB_USER}
EOF

if [ ! -d "~/.my_pgpass" ]; then
    cat << EOF > .pg_service.conf
localhost:5432:NAME:USER:PASSWORD
EOF
