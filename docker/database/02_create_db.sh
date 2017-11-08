#!/bin/bash
set -e # exit immediately if a command exits with a non-zero status.

POSTGRES="psql --username ${POSTGRES_USER}"

# create database
echo "Creating database: ${DB_NAME}"
$POSTGRES <<EOSQL
CREATE DATABASE ${DB_NAME} OWNER ${DB_USER};
EOSQL

# TODO: move this somewhere else?
# create testing database
echo "Creating database: test_db"
$POSTGRES <<EOSQL
CREATE DATABASE test_db OWNER ${POSTGRES_USER};
EOSQL