from flask import jsonify
from app import app
from app.planning_hour import google_api
import populartimes
import os

@app.route('/api/v1/rush_hour/<google_id>', methods=['GET'])
def rush_hour(google_id):
    j_response = populartimes.get_id(os.environ['API_KEY'],google_id)
    return j_response

