from flask import render_template
from strategies.strategy_patterns import get_price_at_date
from datetime import datetime
import pandas as pd

# User's asset data
user_assets = []

# Function to handle portfolio calculation
def handle_calculate_portfolio():
    portfolio_data = calculate_portfolio_data()
    return portfolio_data

# Endpoint to calculate and display the asset portfolio
def calculate_portfolio():
    portfolio_data = handle_calculate_portfolio()
    return render_template('portfolio_summary.html', table_html=portfolio_data)

# Function to calculate portfolio data
def calculate_portfolio_data():
    portfolio_summary = []
    asset_summary = {}

    for asset_data in user_assets:
        asset = asset_data["Asset"]
        quantity = asset_data["Quantity"]
        purchase_price = asset_data.get("Purchase Price", 0)

        if asset not in asset_summary:
            asset_summary[asset] = {"Total Quantity": 0, "Total Cost": 0}
        asset_summary[asset]["Total Quantity"] += quantity
        asset_summary[asset]["Total Cost"] += quantity * purchase_price

    for asset, data in asset_summary.items():
        unit_price = get_price_at_date(asset, datetime.now().strftime('%d-%m-%Y'))
        current_value = data["Total Quantity"] * unit_price
        profit_loss = current_value - data["Total Cost"]
        profit_loss_percentage = (profit_loss / data["Total Cost"]) * 100 if data["Total Cost"] != 0 else 0

        portfolio_summary.append({
            "Asset": asset,
            "Total Quantity": data["Total Quantity"],
            "Purchase Price (TL)": data["Total Cost"] / data["Total Quantity"] if data["Total Quantity"] != 0 else 0,
            "Current Price (TL)": unit_price,
            "Total Cost (TL)": data["Total Cost"],
            "Current Value (TL)": current_value,
            "Profit/Loss (TL)": profit_loss,
            "Profit/Loss Percentage (%)": profit_loss_percentage
        })

    return pd.DataFrame(portfolio_summary).to_html(classes='table table-striped', index=False)
