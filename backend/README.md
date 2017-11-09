# Flask-REST-Backend-Microservice

## Development server

Run `python app.py` to start development server on port `8081` to watch files and restart on update.

## Use from docker container

Clone project on your remote machine (needs to have docker daemon installed), then build image (`docker build -t flask-backend .`) and finally run the image by using `docker run -p 8022:22 -p 8081:8081 -v /HOST/PATH/TO/BACKEND/FOLDER:/app flask-backend`. 

To debug remotely connect to the docker container with ssh (credentials: `root:screencast`) on port `8022`, e.g. for using the python3 executable inside an IDE. 

## Migration commands

See [flask-migrate](https://flask-migrate.readthedocs.io/en/latest/) for more detailed explanation.

### Recreate migrations

Remove `migrations` directory and run `python manage.py db init` and then `python manage.py db migrate`.

### Update database schema

1. Update your database schema (e.g. in `models.py`). Then run `python manage.py db migrate`.
2. Check migration script and use `python manage.py db upgrade` to commit changes to database schema. 
3. Commit changes to git repository.

 
## Execute unit tests

Run `python manage.py test` to execute all test cases in `./tests` directory (must start with `test_`).
