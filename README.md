Simple POC how to use server_default time with sqlalchemy, alembic and PostgreSQL

## Requirements
* Docker
* Python3.9

## Run
Create database
```commandline
docker-compose up
```

Install requrements
```commandline

python3.9 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

```

Apply migrations
```commandline
alembic upgrade head
```

Run text example
```commandline
python .
```
