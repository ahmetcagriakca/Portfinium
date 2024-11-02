# Portfinium

**Portfinium** is a simple yet powerful tool for managing your financial assets, built with Flask. Track, analyze, and visualize your portfolio effortlessly with real-time market data integration.

## Features
- Add and manage multiple financial assets in your portfolio.
- Fetch real-time price data using Yahoo Finance integration.
- Calculate and display portfolio summary, including profit/loss calculations.

## Project Structure
- **app.py**: Main entry point for the Flask application.
- **endpoints/**: Contains endpoint definitions for various functionalities.
  - **add_asset_endpoint.py**: Handles adding new assets.
  - **get_price_endpoint.py**: Fetches asset prices.
  - **calculate_portfolio_endpoint.py**: Manages portfolio calculations.
- **strategies/**: Implements the strategy pattern for fetching and calculating asset prices.
  - **strategy_patterns.py**: Contains different strategies for asset price calculations.
- **templates/**: HTML templates used for rendering pages.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/portfinium.git
   ```
2. Navigate to the project directory:
   ```sh
   cd portfinium
   ```
3. Create a virtual environment:
   ```sh
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source venv/bin/activate
     ```
5. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
6. Run the application:
   ```sh
   python app.py
   ```

## Usage
- Visit `http://127.0.0.1:5000` in your browser.
- Add assets, fetch their prices, and view your portfolio summary.

## Future Improvements
- Add user authentication for personalized asset tracking.
- Integrate a database for persistent storage of portfolio data.
- Enhance the UI with modern front-end frameworks.

## License
This project is open source and available under the [MIT License](LICENSE).
