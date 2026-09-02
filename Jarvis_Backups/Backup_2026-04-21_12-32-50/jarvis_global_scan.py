import yfinance as yf

def scan_global_opportunities():
    # Duniya ki top giants par nazar
    global_stocks = {
        "AAPL": "Apple (USA) - Tech Leader",
        "TSLA": "Tesla (USA) - EV Giant",
        "ASML": "ASML (Europe) - Chip Machines",
        "7203.T": "Toyota (Japan) - Auto Leader"
    }
    
    print("\n[JARVIS] GLOBAL MARKET SCANNING INITIATED...")
    print("--------------------------------------------------")
    
    for ticker, desc in global_stocks.items():
        try:
            stock = yf.Ticker(ticker)
            price = stock.history(period='1d')['Close'][-1]
            currency = stock.info.get('currency', 'USD')
            
            print(f"🌍 {desc}")
            print(f"   >> Price: {price:.2f} {currency}")
            
            # Takeover Calculation (Small Scale Idea)
            mkt_cap = stock.info.get('marketCap', 0)
            print(f"   >> Takeover Cost (51%): {((mkt_cap * 0.51) / 1e9):.2f} Billion {currency}")
            print("-" * 30)
        except Exception as e:
            print(f"⚠️ {ticker} scan error: {e}")

if __name__ == "__main__":
    scan_global_opportunities()
