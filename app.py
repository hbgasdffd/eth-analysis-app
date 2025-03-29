import streamlit as st
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

def main():
    st.title("💰 Real-Time Ethereum Price Dashboard")
    
    # Fetch ETH price
    eth_data = cg.get_price(ids='ethereum', vs_currencies='usd', include_market_cap=True)
    eth_price = eth_data['ethereum']['usd']
    eth_mcap = eth_data['ethereum']['usd_market_cap']
    
    # Display metrics
    st.metric("Current Price", f"${eth_price}")
    st.metric("Market Cap", f"${eth_mcap:,.0f}")
    
    # Optional: Add a line chart (example)
    historical_data = cg.get_coin_market_chart_by_id(id='ethereum', vs_currency='usd', days=7)
    prices = [entry[1] for entry in historical_data['prices']]
    st.line_chart(prices)

if __name__ == "__main__":
    main()