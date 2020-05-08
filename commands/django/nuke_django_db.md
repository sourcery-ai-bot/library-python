# Nuke Postgres Database with Django to Completely Start Again

This should only be completed when I am positive that I am happy to start again from afresh.

### Delete all Project Migration Files

This must be run from the project's source directory

```sh
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
```

### Enter the shell for the Postgres service within the Docker container

```sh
docker exec -it {name_of_postgres_container_in_docker} /bin/sh
```

### Enter the postgres CLI

```sh
psql
```

### Revoke and Terminate Any Existing Connections to the Database

```sql
REVOKE CONNECT ON DATABASE FROM PUBLIC;
select pg_terminate_backend(pid) from pg_stat_activity where datname='{name_of_database}';
```

At this stage, all connections should have been terminated and you will see `pg_terminate_backend` within the `psql` shell

```sh
\q      # Exit out of `psql` shell
exit    # Exit out of the `postgres` service's shell environment
```

### Reset the Database

This part of the process depends upon django-extensions being installed on the project

```sh
docker-compose exec web python manage.py reset_db
```

### Rebuild the Project's Docker build

```sh
docker-compose down
docker system df -v
docker system prune
docker volume rm {any_unsed_volume_name}    # Tidy up unused volumes
docker-compose build
docker-compose up
```

### Migrate Each of the Apps Individually

Repeat this process for each of the apps to give a distinct history within the migrations folders

```sh
docker-compose exec web python manage.py makemigrations {app_name}
```

### Perform the Database Migration

```sh
docker-compose exec web python manage.py migrate
```

### Create a New Superuser

```sh
docker-compose exec web python manage.py createsuperuser
```

I can now connect to the database again in VS Code or DataGrip.

Useful Article: <https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html>
