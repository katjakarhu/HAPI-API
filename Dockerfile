 FROM python:3.5.2
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /code
 WORKDIR /code
 RUN apt-get update && apt-get install netcat-traditional
 ADD requirements.txt /code/
 RUN pip install -r requirements.txt
 ADD . /code/