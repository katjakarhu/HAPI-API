# HAPI-API

# Run with Docker

1. Instal Docker and Docker Compose
2. Run 

```
docker-compose build
docker-compose up
```
3. Result: postgres and web server started at localhost

If something goes wrong, remove Docker containers with `docker-compose rm` and start again.

Note: sets up and uses PostgreSQL instead of SQLite


# Running Hapi Server without Docker

NOTE: CHANGE DATABASE ENGINE TO SQLITE in settings.py. Comment out postgres and uncomment sqlite stuff

The Hapi API is built on Python3, Django and Django Rest Framework.

1. Install requirements: 
```
   pip install -r hateapi/requirements.txt
```

2. Run migrations and start server (it will start at https://localhost:8000 by default):

```
   python3 manage.py migrate
   python3 manage.py runsslserver
```


# Accessing API via Urls

URL check functionality can be found in with an url as a parameter: https://localhost:8000/urlcheck/v1/http://www.google.com//


Full fake site JSON listing can be found in: https://localhost:8000/fakenews/v1/


Detail view per site (parameter is id-number, in the example it's 1): ttps://localhost:8000/fakenews/v1/1/

JSON example:

```
    {
        "id": 1,
        "name": "100PercentFedUp.com",
        "url": "http://100percentfedup.com/",
        "source_name": "Melissa Zimdars / DailyDot",
        "source_url": "http://www.dailydot.com/layer8/fake-news-sites-list-facebook/",
        "source_extra_info": "2, 3",
        "comment_from_api": "Sites where category >= 2 and URL available",
        "created": "2016-12-03T10:47:00Z",
        "created_by": 0,
        "updated": "2016-12-03T10:47:00Z"
    },
    ```
