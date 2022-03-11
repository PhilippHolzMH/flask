import json
import os
from flask import Flask, Blueprint
from flaskr.list_and_count import list_and_count

api_bp = Blueprint("api", __name__)

@api_bp.route('/bucket/<bucket>')
def buckets(bucket): 
    result = list_and_count(bucket)
    return json.dumps(result,indent=4,sort_keys=True)
    

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(api_bp)

    return app