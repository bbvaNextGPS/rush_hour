from flask import Blueprint
from flask import request
from flask import jsonify
import populartimes
import os

root = Blueprint('root', __name__, url_prefix='/')


@root.route('/api/v1/rush_hour/<google_id>', methods=['GET'], )
def rush_hour(google_id):
    current = request.args.get('current')
    j_response = populartimes.get_id(os.environ['API_KEY'], google_id)
    if current == 'true':
        if 'current_popularity' in j_response:
            return jsonify(
                occupancy=j_response['current_popularity']
            )
        else:
            return jsonify(
                occupancy=None
            )
    else:
        return j_response
