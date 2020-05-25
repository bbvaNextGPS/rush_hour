from flask import Blueprint
from flask import request
from flask import jsonify
import populartimes
import os

from app.util import popular_date

root = Blueprint('root', __name__, url_prefix='/')


@root.route('/api/v1/rush_hour/<google_id>', methods=['GET'], )
def rush_hour(google_id):
    fields = request.args.get('fields')
    timeOffset = request.args.get('timezoneOffset')
    j_response = populartimes.get_id(os.environ['API_KEY'], google_id)
    if fields:
        if 'populartimes' in j_response.keys():
            return jsonify(
                {fields: popular_date.get_current_popularity(j_response, int(timeOffset))}
            )
        else:
            return jsonify(
                None
            )
    else:
        return j_response
