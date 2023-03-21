import requests


def api_response(ws, location):
    # Receive the url\
    url = ws.base_url + '?key=' + ws.key + '&q=' + location

    r = requests.get(url)
    response_dict = r.json()

    if len(response_dict) == 0:
        return ''
    else:
        return response_dict
