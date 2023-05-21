#/bin/bash

docker-compose build
docker-compose up -d postgres_db
sleep 10
docker-compose stop postgres_db
sleep 3
docker rm postgres_db