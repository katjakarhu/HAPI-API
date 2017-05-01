# HAPI-API

HAPI-API provides a listing of fake news (as in propaganda / disinform with the intent ofd causing harm) sites.


# Run with Docker

1. Instal Docker and Docker Compose
2. Run 

```
docker-compose build
docker-compose up
```

Result: postgres and web server started at localhost

If you want to run manage.py, login to docker container:

```
 docker ps # get container name from the output, and set as a parameter to next container
 docker exec -t -i <your_container> bash
```


If something goes wrong, remove Docker containers with 
```
   docker-compose kill *
   docker-compose rm
```

and GOTO 2.

If something goes wrong, remove Docker containers with `docker-compose rm` and start again.

Note: sets up and uses PostgreSQL instead of SQLite


# Running Hapi Server without Docker

NOTE: CHANGE DATABASE ENGINE TO SQLITE in settings.py. Comment out postgres and uncomment sqlite stuff

The Hapi API is built on Python3, Django and Django Rest Framework.

1. Install requirements: 
```
   pip install -r hapi-api/requirements.txt
```

2. Run migrations and start server (it will start at https://localhost:8000 by default):

```
   python3 manage.py migrate
   python3 manage.py runsslserver
```

# Admin site

Create admin user:

```
python manage.py createsuperuser
```

Login with created user at https://localhost:8000/admin/

You can edit site data, create users and user tokens for user authentication.


# User authentication: getting token

We use token authentication: http://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication

See Admin site -part for creating users. 

User can get the token at https://localhost:8000/api-token-auth/ by username and password.

From the instruction link above: "The obtain_auth_token view will return a JSON response when valid username and password fields are POSTed to the view using form data or JSON:"

```
{ 'token' : '9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b' }
```

# User authentication: how to implement on client side


For clients to authenticate, the token key should be included in the Authorization HTTP header. The key should be prefixed by the string literal "Token", with whitespace separating the two strings. For example:

```
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

More details here: http://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication


# API Throttling

Anonymous users can make 100 requests per day.

Authenticated users can make 10000 requests per day. 

These are set in `settings.py` -> `DEFAULT_THROTTLE_RATES`


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
