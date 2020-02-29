#!/bin/bash

# Remove any Django migrations
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
# Django setup commands
docker-compose exec web python3 manage.py makemigrations users
docker-compose exec web python3 manage.py makemigrations contacts
docker-compose exec web python3 manage.py makemigrations blog

# Use this command if I have pruned the Docker volume
docker-compose exec web python3 manage.py migrate
# Don't forget to set up my superuser
docker-compose exec web python3 manage.py createsuperuser