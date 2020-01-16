#!/bin/bash
python3 manage.py makemigrations
python3 manage.py migrate
uwsgi --ini /usr/src/app/config/uwsgi/uwsgi.ini --http :8000
