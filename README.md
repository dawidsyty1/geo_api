## The architecture.
    The application is created using Django and DjangoRestFramework, integrated with a Postgresql database.
    I've involved Celery and Redis to make asynchronous tasks.
    It is possible to make an external API call in two mods, by setting ASYNCHRONOUS_ON.    
    Linked uwsgi and nginx using containers.

## Availabale Requests.
```bash

    POST /api/v1/accounts/obtain_token 
    POST /api/v1/accounts/create_user
    GET,POST /api/v1/geolocation/
    GET,DELETE /api/v1/geolocation/<id>/

```
## Example calls.
```bash

    #create new user
    curl --header "Content-Type: application/json" --request POST --data '{"username": "test", "email":"test@test.com", "password": "test"}' http://172.17.0.5:8000/api/v1/accounts/create_user
    #obtain access token
    curl --header "Content-Type: application/json" --request POST --data '{"username": "test", "password": "test"}' http://172.17.0.5:8000/api/v1/accounts/obtain_token
    # get all geolocation data from database
    curl --header "Content-Type: application/json" --header "Authorization: JWT obtained-token" --request GET http://172.17.0.5:8000/api/v1/geolocation/
    # add geolocation data to your data base
    curl --header "Content-Type: application/json" --header "Authorization: JWT obtained-token" --request POST --data '{"url": "www.instagram.com"}' http://172.17.0.5:8000/api/v1/geolocation/

```
##

## Run from docker-compose, before starting the application, you have to set in config/env.secret two variables.
    IPSTACK_PRIVATE_KEY - you can obtain free API KEY here -> https://ipstack.com/signup/free.
    SECRET_KEY - required by Django.

```bash

    docker-compose build
    docker-compose up

```
##
## Load geolocation data fixtures and start test.
```bash
    
    docker-compose exec web python3 manage.py loaddata geolocation/fixtures/geolocation_data.json
    docker-compose exec web python3 manage.py test
```
##
## Get Rest API service address IP.
```bash

    docker-compose exec service_name ip a

```
##



 
