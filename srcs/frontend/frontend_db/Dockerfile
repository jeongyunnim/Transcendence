FROM postgres:alpine3.19

ARG FE_DB
ARG FE_DB_HOST
ARG FE_DB_USER
ARG FE_DB_PW

RUN apk upgrade &&\
	apk add --no-cache\
	dumb-init

WORKDIR /var/lib/postgresql

USER postgres

RUN pg_ctl initdb -D /var/lib/postgresql/data &&\
	echo "host all all 0.0.0.0/0 md5" >> /var/lib/postgresql/data/pg_hba.conf &&\
	echo "listen_addresses='*'" >> /var/lib/postgresql/data/postgresql.conf

RUN pg_ctl start &&\
	psql -U postgres -c "CREATE DATABASE $FE_DB;" && \
    psql -U postgres -d $FE_DB -c "CREATE TABLE $FE_DB (id SERIAL PRIMARY KEY, name VARCHAR(50));" && \
    psql -U postgres -c "CREATE USER $FE_DB_USER WITH PASSWORD '$FE_DB_PW';" && \
    psql -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE $FE_DB TO $FE_DB_USER;" &&\
	pg_ctl stop

ENTRYPOINT [ "dumb-init", "--", "postgres", "-D", "/var/lib/postgresql/data" ]