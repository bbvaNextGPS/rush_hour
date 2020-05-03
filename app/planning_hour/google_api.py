import populartimes

def rush_hours(api_key, google_id):

    r = populartimes.get_id(api_key,google_id)
    return r