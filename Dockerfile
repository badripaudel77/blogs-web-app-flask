FROM python:3.9.16-slim-bullseye

WORKDIR /app

COPY requirements-docker.txt /app

# As installing psycopg2==2.9.3  from requirements.txt gives error because it needs other dependencies as well.
# It has been downloaded here [removed from the .txt file]
# Include psycopg2==2.9.3 if you're trying to run in local dev.
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

RUN pip3 install -r requirements-docker.txt

COPY . /app
    
EXPOSE 5000

ENTRYPOINT ["python3"]

CMD ["main.py"]


