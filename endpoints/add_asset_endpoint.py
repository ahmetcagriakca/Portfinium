from flask import request, render_template
from strategies.strategy_patterns import get_price_at_date
from datetime import datetime

# User's asset data
user_assets = []

# Function to handle adding asset request
def handle_add_asset_request():
    message = ""
    if request.method == 'POST':
        asset = request.form.get("asset")
        quantity = request.form.get("quantity")
        date = request.form.get("date")
        price = request.form.get("price")
        
        if asset and quantity and date and price:
            try:
                quantity = float(quantity)
                price = float(price)
                datetime.strptime(date, "%d-%m-%Y")
                user_assets.append({"Asset": asset, "Quantity": quantity, "Date": date, "Purchase Price": price})
                message = f"Asset added successfully with purchase price of {price:.2f} TL"
            except ValueError:
                message = "Invalid quantity, price, or date format"
        else:
            message = "Invalid data"
    elif request.method == 'GET':
        asset = request.args.get("asset")
        date = request.args.get("date")
        if asset and date:
            price = get_price_at_date(asset, date)
            message = f"Price on {date} for {asset} is {price:.2f} TL" if price else "Price data not available"
    return message

# Function to render the add asset page
def add_asset():
    message = handle_add_asset_request()
    return render_template('add_asset.html', message=message)
