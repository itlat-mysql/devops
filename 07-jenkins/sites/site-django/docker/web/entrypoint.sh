#!/bin/bash

cd /app

echo 'Waiting for mysql...'
while ! nc -z $DB_HOST $DB_PORT; do
  sleep 0.1
done
echo 'MySQL started!'

python manage.py collectstatic --no-input --clear
python manage.py migrate --noinput

if [ ! -f 'configs/db-enabled' ]; then
    python manage.py seed_data
    touch 'configs/db-enabled'
fi

exec "$@"