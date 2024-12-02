#!/bin/bash

# Run migrations
python manage.py makemigrations --no-input
python manage.py migrate --no-input

# Start Django development server
python manage.py runserver 0.0.0.0:8000
