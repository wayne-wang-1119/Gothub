# Set up Django
cd gothub_server/src/gothub_server
python manage.py makemigrations
python manage.py migrate

# Start Django development server
python manage.py runserver 8002
