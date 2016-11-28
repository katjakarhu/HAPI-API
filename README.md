# HAPI-API

# Running Hapi Server

The Hapi API is built on Python3, Django and Django Rest Framework.

1. Install requirements: 

   pip install -r hateapi/requirements.txt

2. Run server (it will start at https://localhost:8000 by default):

   python3 manage.py runsslserver
   
3. Give an URL to the API, you will get a JSON response in return, e.g. type https://localhost:8000/fakenews?url=urlhere&url=secondurl&url=thirdurl
