#!/bin/sh

if [ -z $FE_DB_PW ]; then
  exit 1
fi

POSTGRESQL_BIN=/usr/local/bin/postgres
POSTGRESQL_CONFIG_FILE=/usr/local/share/postgresql/postgresql.conf

POSTGRESQL_SINGLE="$POSTGRESQL_BIN --single --config-file=$POSTGRESQL_CONFIG_FILE"
$POSTGRESQL_SINGLE << "ALTER USER postgres PASSWORD '$FE_DB_PW';" > /dev/null

exec $POSTGRESQL_BIN --config-file=$POSTGRESQL_CONFIG_FILE

