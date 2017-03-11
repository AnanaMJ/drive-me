from flask import Flask, render_template
from uber_rides.session import Session
from uber_rides.client import UberRidesClient
import _json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html')

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
