# OTestTask
My solution for the test task for the O.Dev. for backend internship
## Task:
Create REST API with Django to get different metrics on the window (range) of data
### Technologies:
* Python 3.7.6
* Django 2.2
* Django Rest Framework
* Redis
* PostgreSQL 11
* Swagger (didn't use)
* Docker (didn't use)
## Urls:
* /admin/ **– Admin menu**
* /api/ **– View metrics**
### Query parameters for metrics:
* start_at
* end_at
* base
* 
* Example:
* 127.0.0.1:8000/api/?start_at=2020-04-01&end_at=2020-05-06&base=USD
* 
* You may leave query parameters blank, so default ones will be used:
* start_at = '1999-01-04'
* end_at = today
* base = 'EUR'
## Install:
pip install -r requirements.txt
## Run:
* python manage.py runserver
* ./manage.py runserver
