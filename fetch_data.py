import yfinance as yf
import pandas as pd
import os

# Define the tickers for the 7 FMCG Companies (using Indian market .NS suffix)
FMCG_COMPANIES = {
    "BRITANNIA.NS": "Britannia Industries",
    "HINDUNILVR.NS": "Hindustan Unilever",
    "ITC.NS": "ITC Limited",
    "NESTLEIND.NS": "Nestle India",
    "DABUR.NS": "Dabur India",
    "GODREJCP.NS": "Godrej Consumer Products",
    "MARICO.NS": "Marico Limited"
}

def fetch_financial_metrics():
    print("Initializing data fetch from Yahoo Finance...")
    
    # Ensure data directory exists
    data_dir = os.path.join(os.path.dirname(__file__), "..", "data")
    os.makedirs(data_dir, exist_ok=True)
    
    metrics = []

    for ticker, company_name in FMCG_COMPANIES.items():
        print(f"-> Fetching {company_name} ({ticker})")
        try:
            stock = yf.Ticker(ticker)
            info = stock.info
            
            # Extract key valuation multiples
            pe_ratio = info.get("trailingPE", None)
            pb_ratio = info.get("priceToBook", None)
            ev_ebitda = info.get("enterpriseToEbitda", None)
            market_cap = info.get("marketCap", None)
            
            metrics.append({
                "Company": company_name,
                "Ticker": ticker,
                "Market Cap (INR)": market_cap,
                "P/E Ratio": pe_ratio,
                "P/B Ratio": pb_ratio,
                "EV/EBITDA": ev_ebitda
            })
        except Exception as e:
            print(f"Error fetching {ticker}: {e}")

    # Compile into DataFrame
    df = pd.DataFrame(metrics)
    
    # Save to CSV
    output_file = os.path.join(data_dir, "fmcg_valuation_summary.csv")
    df.to_csv(output_file, index=False)
    print(f"\nSuccess! Valuation data saved to {output_file}")

if __name__ == "__main__":
    fetch_financial_metrics()
