#!/bin/bash
set -e # exit immediately if a command exits with a non-zero status.

POSTGRES="psql --username ${POSTGRES_USER}" # start psql shell with admin user

# create role for airflow
echo "Creating database role: ${DB_USER}"
$POSTGRES <<-EOSQL
CREATE USER ${DB_USER} WITH CREATEDB PASSWORD '${DB_PASSWORD}';
EOSQL