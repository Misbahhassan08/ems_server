# Use the official Python image.
# https://hub.docker.com/_/python
FROM python:3.9

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt


ENV PORT 8080


COPY . /app/

CMD gunicorn --bind :$PORT --workers 3 ems_project.wsgi