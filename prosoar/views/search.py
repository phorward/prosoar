from flask import Blueprint, request

import urllib

bp = Blueprint('search', __name__)


@bp.route('/<bbox>/<q>')
def main(bbox, q):
    url = 'http://nominatim.openstreetmap.org/search/' + q + \
        '?format=json&limit=1&viewbox=' + bbox + '&email=info@prosoar.de'

    try:
        request = urllib.urlopen(url)
        return request.read()

    except:
        return '[]'
