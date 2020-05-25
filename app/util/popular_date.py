import datetime


def get_current_popularity(popular_times, timezone):
    tzinfo = datetime.timezone(datetime.timedelta(hours=timezone))
    locale_date = datetime.datetime.now(tzinfo)
    dayOfWeek = locale_date.strftime("%A")
    for p in popular_times['populartimes']:
        if p['name'] == dayOfWeek:
            return p['data'][locale_date.hour]
