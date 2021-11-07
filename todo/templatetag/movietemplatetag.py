from django.template import Library
import json
import requests

from pprint import pprint
register = Library()

r = requests.get('http://www.omdbapi.com/?s=Runner')

data = json.loads(r.text)

pprint(data)


@register.simple_tag
def my_simple_tag(user):
    return "Hello {} From Tag".format(user)


@register.filter
def get_movie_data(title):
    endpoint = 'http://www.omdbapi.com/'
    param = {}
    param['t'] = title
    param['r'] = 'json'
    this_page_cache = requests.get(endpoint, params=param)

    return json.loads(this_page_cache.text)