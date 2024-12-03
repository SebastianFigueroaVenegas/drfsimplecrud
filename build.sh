#!/usr/bin/env bash
#exit on error

set -o errexit

poetry install

python manage.py collecstatic --no-input
python manage.py migrate