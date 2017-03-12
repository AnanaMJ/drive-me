from flask import Flask, jsonify, make_response
from flask_cors import CORS
import json
import requests
import operator

app = Flask(__name__)
CORS(app)


@app.route(
    '/estimate/startLat=<string:start_lat>&startLon=<string:start_lon>&endLat=<string:end_lat>&endLon=<string:end_lon>')
def estimate(start_lat, start_lon, end_lat, end_lon):
    taxicode = get_taxicode_estimate(start_lat, start_lon, end_lat, end_lon)
    uber = parse_uber(start_lat, start_lon, end_lat, end_lon)
    result = taxicode.copy()
    result.update(uber)
    sorted_result = sorted(result.items(), key=operator.itemgetter(1))

    return jsonify(sorted_result[0:5])


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


def get_taxicode_estimate(start_latitude=None, start_longitude=None, end_latitude=None, end_longitude=None):
    url = 'https://api.taxicode.com/booking/quote/?pickup={},{}&destination={},{}&date=13-03-2017'.format(
        start_latitude, start_longitude, end_latitude, end_longitude)
    r = requests.get(url)

    result = {}

    for item, value in r.json()['quotes'].items():
        company_name = value['company_name']
        for item in value['vehicles']:
            car_name = '{}-{}'.format(company_name, item['name'])
            if 'price' in item:
                result[car_name] = {"high_price": item['price'],
                                    "low_price": item['price']}
    return result


def get_uber_estimate(start_latitude=None, start_longitude=None, end_latitude=None, end_longitude=None):
    url = 'https://sandbox-api.uber.com/v1.2/estimates/price?start_latitude={}&start_longitude={}&end_latitude={}&end_longitude={}'.format(
        start_latitude, start_longitude, end_latitude, end_longitude)
    headers = {'Authorization': 'Token EZx9qEWb2Uvt2_fsukQoNzgl5jvFdcXIJCAcUMEs', 'Content-Type': 'application/json'}
    r = requests.get(url, headers=headers)
    return r.text


def parse_uber(start_latitude, start_longitude, end_latitude, end_longitude):
    uber = {}
    parsed_uber_json = json.loads(get_uber_estimate(start_latitude, start_longitude, end_latitude, end_longitude))
    if 'prices' in parsed_uber_json:
        for uber_type in parsed_uber_json['prices']:
            high_price = uber_type['high_estimate']
            low_price = uber_type['low_estimate']
            uber_type = uber_type['localized_display_name']
            if high_price and low_price:
                uber[uber_type] = {}
                uber[uber_type]['high_price'] = high_price
                uber[uber_type]['low_price'] = low_price
    return uber


def get_hailo_estimate(start_latitude=None, start_longitude=None, end_latitude=None, end_longitude=None):
    url = 'https://api.hailoapp.com/drivers/eta?latitude={}&longitude={}&destinationCoordinate={},{}'.format(
        start_latitude, start_longitude, end_latitude, end_longitude)
    headers = {'Host': 'api.hailoapp.com',
               'Accept': '*/*',
               'Authorization': 'token Z7r9oJePCMy2WkCGoI3PtNOWCGe9L2LroLF6wxUI6EfXg+knJdB4ZMp2BLpTjDroFr6Tp52FVBUzuMlgRnC/A/2hlL017T3lNnvcPTNvMlVV4Uxs0IhEyC2h0OKg+9QDN58DXgbO3y1itg4KWv0pwvbFX6ZQfvasHsPTeLpEAERkB4xS2fZZosYo137jWSangjdPndI+GzMaxtc4AFvueA=='}
    r = requests.get(url, headers=headers)
    return r.text


if __name__ == '__main__':
    app.run()
