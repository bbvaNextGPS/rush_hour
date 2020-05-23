from flask import Blueprint
from flask import request
from flask import jsonify
import populartimes
import os

root = Blueprint('root', __name__, url_prefix='/')


@root.route('/api/v1/rush_hour/<google_id>', methods=['GET'], )
def rush_hour(google_id):
    fields = request.args.get('fields')
    j_response = populartimes.get_id(os.environ['API_KEY'], google_id)
    if fields:
        if fields in j_response.keys():
            return jsonify(
                {fields: j_response[fields]}
            )
        else:
            return jsonify(
                None
            )
    else:
        return j_response
