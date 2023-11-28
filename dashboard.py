import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
from datetime import datetime
import requests
import pandas as pd

def get_top_coins_by_volume(limit=20, days=90):
    # CoinGecko API endpoint for coins/markets
    api_endpoint = "https://api.coingecko.com/api/v3/coins/markets"
    historical_data_endpoint = "https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"

    # Parameters for the API request
    params = {
        'vs_currency': 'usd',
        'order': 'volume_desc',  # Sort by volume in descending order
        'per_page': limit,
        'page': 1,  # Adjust the page number if you want more than 20 coins
    }

    try:
        # Make the API request
        response = requests.get(api_endpoint, params=params)
        data = response.json()

        coin_info = []
        for coin_data in data:
            coin_id = coin_data['id']
            coin_name = coin_data['name']
            coin_symbol = coin_data['symbol']

            # Get historical price data
            historical_params = {
                'vs_currency': 'usd',
                'days': days,
            }
            historical_response = requests.get(historical_data_endpoint.format(coin_id=coin_id), params=historical_params)
            historical_data = historical_response.json()
            prices = historical_data.get('prices', [])

            coin_info.append({
                'Name': coin_name,
                'Symbol': coin_symbol,
                'Prices': prices
            })

        df = pd.DataFrame(coin_info)
        return df

    except Exception as e:
        print(f'Error: {e}')



# Function to add logo
def add_logo(logo_path, width, height):
    logo = Image.open(logo_path)
    modified_logo = logo
    return modified_logo

# Home page
def home():
    st.title("Home Page")
    st.write("Welcome to the home page!")

# Page 1
def page1():
    st.title("Charts")
    st.write("TV")
    html_string = '''
 <!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container" style="height:500px;width:100%">
  <div id="tradingview_828e6" style="height:calc(100% - 32px);width:100%"></div>
  <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/" rel="noopener nofollow" target="_blank"><span class="blue-text">Track all markets on TradingView</span></a></div>
  <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
  <script type="text/javascript">
  new TradingView.widget(
  {
  "autosize": true,
  "symbol": "SPY",
  "interval": "D",
  "timezone": "Etc/UTC",
  "theme": "dark",
  "style": "1",
  "locale": "en",
  "enable_publishing": false,
  "allow_symbol_change": true,
  "container_id": "tradingview_828e6"
}
  );
  </script>
</div>
<!-- TradingView Widget END -->
'''

    components.html(html_string, height=500)  # JavaScript works

# Page 2
def page2():
    st.title("Page 2")
    st.write("Correlation Heatmap")
    coin_data = get_top_coins_by_volume()
    
    # Extract price data and create a DataFrame
    prices_df = pd.DataFrame({coin['Name']: [price[1] for price in coin['Prices']] for coin in coin_data['Prices']})
    
    # Calculate price correlations
    correlations = prices_df.corr()

    # Display heatmap
    st.write("Price Correlations Heatmap (last 90 days)")
    st.write(correlations.style.background_gradient(cmap='coolwarm'))

# Main App
def main():
    st.set_page_config(layout="wide")
    #st.title("Cavins Investment Research")

    # Add logo to sidebar
    my_logo = add_logo(logo_path="./logo_3.png", width=300, height=250)
    st.sidebar.image(my_logo)

    # Create a sidebar menu for navigation
    pages = {"Home": home, "charts": page1, "crypto dashboard": page2}
    selected_page = st.sidebar.radio("Select a page", list(pages.keys()))

    # Display the selected page
    pages[selected_page]()


if __name__ == "__main__":
    main()