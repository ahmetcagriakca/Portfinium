import pandas as pd
import requests
from flask import Flask
from endpoints.add_asset_endpoint import add_asset
from endpoints.get_price_endpoint import get_price
from endpoints.calculate_portfolio_endpoint import calculate_portfolio

# Create Flask application
app = Flask(__name__)

# Registering endpoints
app.add_url_rule('/add_asset', view_func=add_asset, methods=['GET', 'POST'])
app.add_url_rule('/get_price', view_func=get_price, methods=['GET'])
app.add_url_rule('/calculate_portfolio', view_func=calculate_portfolio, methods=['GET'])

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
