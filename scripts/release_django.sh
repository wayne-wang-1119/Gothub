cd gothub_server/src/
# PYTHON="/home/kingh/disk-1/miniconda3/envs/gothub/bin/python"
# $PYTHON manage.py runserver 0.0.0.0:80
# $PYTHON manage.py runserver 0.0.0.0:80 --cert /tmp/cert

python -m gunicorn gothub_server.wsgi:application --bind 127.0.0.1:8000
