from flask import Flask, render_template
#from uber_rides.session import Session
#from uber_rides.client import UberRidesClient
import json

import requests

app = Flask(__name__)


@app.route('/')
def index():
    start_latitude = '51.5254506'
    start_longitude = '-0.1292581'
    end_latitude = '51.5114864'
    end_longitude = '-0.1181857'
    return get_taxicode_estimate(start_latitude, start_longitude, end_latitude, end_longitude)

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
    return r.text

def create_session():
    session = Session(server_token= "EZx9qEWb2Uvt2_fsukQoNzgl5jvFdcXIJCAcUMEs")
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
