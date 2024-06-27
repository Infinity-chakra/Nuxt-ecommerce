![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![Django Rest Framework](https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white)
![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)

# Ecommerce API created using Myntra dataset

This is an Ecommerce API which I created using a dataset with data taken from https://myntra.com which is one of the most popular online clothing stores in India.

http://localhost:8000/api-docs/

The API docs can be viewed using the above link. Swagger is used to generate API docs under the hood using a package called 'drf_spectacular'.

## Getting Started

* Create a new virtual environment and install packages specified in the requirements.txt file.

* Hook in your database of choice, make necessary database changes in the settings.py file inside the project folder. Obviously, some familiarity with Django folder structures is required for this. By default this project uses MySQL as database.

* Make migrations when you're done with the database settings and migrate.
* Run python manage.py runserver, and the application should be running on port 8000 by default.

## Built With

* [Python Django](https://www.djangoproject.com/)
* [Django Rest Framework](https://www.django-rest-framework.org/)
* [Swagger Docs](https://swagger.io/)

## Features 

Application has around 10K entries for clothing related products coming from a dataset I retrieved from Kaggle.com
For feeding the data into the database, Management commands are used.

```
python manage.py populate
python manage.py clear
```

Populate command reads the csv file and creates an item model for each row saving it in the database. Clear command is as the name suggests clears the database in case required in any case.

The initial data was kind of large so I had to condense it by only picking the first 10k entries from the csv file. It was done using the pandas library.

```
import pandas as pd

def condense_data():

    # Read data from csv file
    df = pd.read_csv('data/myntra.csv')

    # Read only first 5k enties and save it in a new csv file

    df = df.head(5000)
    df.to_csv('data/myntra_condensed.csv')


condense_data()

```

## Updates

React frontend to be added in future.

### Added Support for MySQL

Install pymysql library

```
pip install pymysql
```

Import it in settings.py file

```
import os
from pathlib import Path
import pymysql
pymysql.install_as_MySQLdb()

...
```

Database configuration

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myntra',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'localhost',   # Or the IP Address where your MySQL server is hosted
        'PORT': '3306',        # Default MySQL port
    }
}
```

Run Migrations and populate data from the dataset.

```
python manage.py migrate
python manage.py populate
```

Taking Database Back-up

```
python manage.py db_backup [--filename <filename>] [--database <database_name>]

python manage.py db_backup --filename myntra_backup.sql --database myntra

```

## API Throttling

API throttling is a concept of limiting the user access to a specific number based on the privileges of the user. In this application we allow logged in users to 10 requests/min and anonymous users to 5 req/min.

```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAUL_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '5/min',
        'user': '10/min',
    },
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 50,
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}
```

## Authors

* **Amit Prafulla (APFirebolt)** - (http://apgiiit.com/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

```
docker-compose run --rm web python manage.py populate

docker-compose build --no-cache

docker run -d \
  -p 5173:5432 \
  --name my-postgres \
  -e POSTGRES_DB=myntra \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=pass123 \
  postgres:latest


docker-compose up
```

```
docker-compose down -v
```

## Screenshots

## Screenshots

Swagger Documentation 

![Screenshot 1](screenshots/1.png)

REST FRAEMWORK view of the items page.

![Screenshot 2](screenshots/2.png)


