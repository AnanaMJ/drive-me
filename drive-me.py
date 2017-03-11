from flask import Flask, render_template
# from uber_rides.session import Session
# from uber_rides.client import UberRidesClient
import json

from flask import jsonify
import requests
import operator

app = Flask(__name__)


@app.route('/')
def index():
    start_latitude = '51.5254506'
    start_longitude = '-0.1292581'
    end_latitude = '51.5114864'
    end_longitude = '-0.1181857'
    taxicode = get_taxicode_estimate(start_latitude, start_longitude, end_latitude, end_longitude)
#    sorted_result = sorted(taxicode.items(), key=operator.itemgetter(1))
    uber = parse_uber(start_latitude, start_longitude, end_latitude, end_longitude)
    result = taxicode.copy()
    result.update(uber)
    return jsonify(result)


def get_uber_estimate(start_latitude=None, start_longitude=None, end_latitude=None, end_longitude=None):
    url = 'https://api.uber.com/v1.2/estimates/price?start_latitude={}&start_longitude={}&end_latitude={}&end_longitude={}'.format(
        start_latitude, start_longitude, end_latitude, end_longitude)
    headers = {'Authorization': 'Token EZx9qEWb2Uvt2_fsukQoNzgl5jvFdcXIJCAcUMEs', 'Content-Type': 'application/json'}
    r = requests.get(url, headers=headers)
    return r.text


def get_taxicode_estimate(start_latitude=None, start_longitude=None, end_latitude=None, end_longitude=None):

    url = 'https://api.taxicode.com/booking/quote/?pickup={},{}&destination={},{}&date=13-03-2017'.format(
        start_latitude, start_longitude, end_latitude, end_longitude)
    r = requests.get(url)

    result = {}

    for item, value in r.json()['quotes'].items():
        company_name = value['company_name']

        for item in value['vehicles']:
            car_name = '{}-{}'.format(company_name, item['name'])
            result[car_name] = {"high_price": item['price'],
                                "low_price": item['price']}

    return result


def get_hailo_estimate(start_latitude=None, start_longitude=None, end_latitude=None, end_longitude=None):
    url = 'https://api.hailoapp.com/drivers/eta?latitude={}&longitude={}&destinationCoordinate={},{}'.format(
        start_latitude, start_longitude, end_latitude, end_longitude)
    headers = {'Host': 'api.hailoapp.com',
               'Accept': '*/*',
               'Authorization': 'token Z7r9oJePCMy2WkCGoI3PtNOWCGe9L2LroLF6wxUI6EfXg+knJdB4ZMp2BLpTjDroFr6Tp52FVBUzuMlgRnC/A/2hlL017T3lNnvcPTNvMlVV4Uxs0IhEyC2h0OKg+9QDN58DXgbO3y1itg4KWv0pwvbFX6ZQfvasHsPTeLpEAERkB4xS2fZZosYo137jWSangjdPndI+GzMaxtc4AFvueA=='}
    r = requests.get(url, headers=headers)
    return r.text

def parse_uber(start_latitude, start_longitude, end_latitude, end_longitude):
    uber = {}
    parsed_uber_json = json.loads(get_uber_estimate(start_latitude, start_longitude, end_latitude, end_longitude))
    for uber_type in parsed_uber_json['prices']:
        high_price = uber_type['high_estimate']
        low_price = uber_type['low_estimate']
        uber_type = uber_type['localized_display_name']
        if high_price and low_price:
            uber[uber_type] = {}
            uber[uber_type]['high_price'] = high_price
            uber[uber_type]['low_price'] = low_price

    return uber


def create_session():
    session = Session(server_token="EZx9qEWb2Uvt2_fsukQoNzgl5jvFdcXIJCAcUMEs")
    client = UberRidesClient(session)
    return client


def get_products():
    client = create_session()
    response = client.get_products(37.77, -122.41)
    products = response.json.get('products')


def get_estimates():
    client = create_session()
    response = client.get_products(37.77, -122.41)
    products = response.json.get('products')

    response = client.get_price_estimates(
        start_latitude=37.770,
        start_longitude=-122.411,
        end_latitude=37.791,
        end_longitude=-122.405,
        seat_count=2
    )

    estimate = response.json.get('prices')


if __name__ == '__main__':
    app.run()
