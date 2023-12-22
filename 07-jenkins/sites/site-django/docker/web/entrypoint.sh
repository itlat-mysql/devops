#!/bin/bash

cd /app

echo 'Waiting for mysql...'
while ! nc -z $DB_HOST $DB_PORT; do
  sleep 0.1
done
echo 'MySQL started!'

python manage.py collectstatic --no-input --clear
python manage.py migrate --noinput

if [ "${DJANGO_SEED_DATA}" -eq 1 ]; then
    python manage.py seed_data
fi

exec "$@"