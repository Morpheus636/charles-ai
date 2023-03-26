# Development Scripts

- `make start-db`
  - Starts the local postgres and pgadmin instances in docker containers. It will print the connection info to the
    console once the containers are started.
  - The username and password for pgadmin are set in docker-compose-postgres.yml.
  - Postgres tries to load the database data from docker_pgsql_volume if it's present. 
    If not, it runs the initdb.sh script in docker_pgsql_init, which is where the postgres login and database name are set.

- `make stop-db`
  - Stops the containers started by the above script.