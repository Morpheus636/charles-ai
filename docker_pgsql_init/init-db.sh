#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER localdev WITH PASSWORD 'localdev_secret';
    CREATE DATABASE replaceme;
    GRANT ALL PRIVILEGES ON DATABASE replaceme TO localdev;
EOSQL