#!/bin/bash

cd /app

python manage.py collectstatic --no-input --clear
python manage.py migrate --noinput

if [ ! -f 'db-enabled' ]; then
    python manage.py seed_data
    touch 'db-enabled'
fi

python manage.py runserver 0.0.0.0:80