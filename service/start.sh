#!/bin/bash
#version=1.0
dev_url="/usr/local/developer/"
prod_url="/usr/local/docker/"
proj_name="sss-fastapi-service"


#sss-personal-web package create docker image and start container
git pull
docker-compose down
docker build -t ${proj_name} .
docker image prune -f
docker-compose up -d
