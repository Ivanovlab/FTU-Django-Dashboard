#!/bin/sh

set -e

# Django management command that collects all static command and
#   stores them in the root for more efficient deployment and
#   server
python manage.py collectstatic --no-input

uwsgi --socket :8000 --master --enable-threads --module app.wsgi
