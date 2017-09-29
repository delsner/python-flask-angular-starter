# Flask-REST-Backend-Microservice

## Development server

Run `python app.py` to start development server on port `8081` to watch files and restart on update.

## Use from docker container

Clone project on your remote machine (needs to have docker daemon installed), then build image (`docker build -t flask-backend .`) and finally run the image by using `docker run -p 8022:22 -p 8081:8081 -v /HOST/PATH/TO/BACKEND/FOLDER:/app flask-backend`. 

To debug remotely connect to the docker container with ssh (credentials: `root:screencast`) on port `8022`, e.g. for using the python3 executable inside an IDE. 

