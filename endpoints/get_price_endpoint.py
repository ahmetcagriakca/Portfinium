from flask import request, jsonify
from strategies.strategy_patterns import get_price_at_date

# Function to handle price request
def handle_get_price_request():
    asset = request.args.get("asset")
    date = request.args.get("date")
    if asset and date:
        try:
            purchase_price = get_price_at_date(asset, date)
            return {"message": f"Price on {date} for {asset} is {purchase_price:.2f} TL", "price": purchase_price}
        except ValueError:
            return {"message": "Invalid date format", "price": 0}
    return {"message": "Invalid data", "price": 0}

# Endpoint to get price for a given asset and date
def get_price():
    response = handle_get_price_request()
    return jsonify(response)
