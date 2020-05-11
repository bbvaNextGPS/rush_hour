from flask import Blueprint
import populartimes
import os

root = Blueprint('root', __name__, url_prefix='/')

@root.route('/api/v1/rush_hour/<google_id>', methods=['GET'])
def rush_hour(google_id):
    j_response = populartimes.get_id(os.environ['API_KEY'], google_id)
    return j_response

@root.route("api/v1/", methods=['GET'])
def helloWorld():
    return "Hello, cross-origin-world!"
