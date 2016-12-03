# HAPI-API

# Running Hapi Server

The Hapi API is built on Python3, Django and Django Rest Framework.

1. Install requirements: 

   pip install -r hateapi/requirements.txt

2. Run server (it will start at https://localhost:8000 by default):

   python3 manage.py runsslserver
   

URL check functionality can be found in with <url> as parameter: https://localhost:8000/fakenewsurlcheck/v1/<url>/
Full fake site JSON listing can be found in: https://localhost:8000/fakenews/v1/
Detail view per site (parameter is id-number, in the example it's 1): ttps://localhost:8000/fakenews/v1/1/
