from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy

# local imports
from instance.config import app_config

# initialize sql-alchemy
db = SQLAlchemy()

def create_app(config_name):

    # initialize flask app
    app = FlaskAPI(__name__, instance_relative_config=True)

    # configuration
    app.config.from_object(app_config[config_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)


    # add routes/blueprints
    from app.api.cluster import cluster_api
    app.register_blueprint(cluster_api, url_prefix='/clusters')

    return app
