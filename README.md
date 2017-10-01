# Webapp Starter with Flask REST API Backend and MongoDB

NOTE: There could occur problems running this on windows.

## Development web backend/frontend

If desired, you can add a custom host in your hosts file (e.g. `127.0.0.1   db`). 
Thus, the server config won't need any more configuration for production.

### Docker development

I recommend using docker because it's just one command and everything is up and running:

Run `docker-compose -f docker-compose.dev.yml up`.

This will fire up a mongodb, backend and frontend and watch files for your local changes.  

### Backend development

Only if you prefer developing without using docker.

Run `./install.sh` in the backend directory.

Run `python app.py` in backend root (will watch files and restart server on port `8081` on change).
In order to install new packages, add them to the `requirements.txt` file. If you run the `watcher.py` (default when using docker) they will be automatically installed in the background so you can use them in your app.

### Frontend development

Only if you prefer developing without using docker.

Run `yarn install` in the frontend directory.

Run `yarn start` in frontend root (will watch files and restart dev-server on port `4200` on change). 
All calls made to `/api` will be proxied to backend server (default port for backend `8081`), this can be changed in `proxy.conf.json`.

## Production web backend/frontend

Run `docker-compose up` in root. Will start four containers (mongodb, backend, frontend, nginx). 
