import yfinance as yf

# Jarvis Top 5 Future-Ready Stocks (2026-2030)
FUTURE_GEMS = {
    "TATASTEEL.NS": "Infrastructure & Green Steel",
    "TATAPOWER.NS": "EV Charging & Solar Energy",
    "IREDA.NS": "Renewable Energy Financing",
    "NVDA": "AI Chips (Global Leader)",
    "KPITTECH.NS": "Autonomous Driving Software"
}

def load_future_gems():
    print("==================================================")
    print("        JARVIS STRATEGIC WATCHLIST: LOADED        ")
    print("==================================================")
    print("Sector: AI, Green Energy & Advanced Robotics")
    print("--------------------------------------------------")
    
    for ticker, sector in FUTURE_GEMS.items():
        try:
            stock = yf.Ticker(ticker)
            price = stock.history(period='1d')['Close'][-1]
            currency = "INR" if ".NS" in ticker else "USD"
            
            print(f"💎 {ticker} | {sector}")
            print(f"   >> Current Price: {price:.2f} {currency}")
            
            # Jarvis Ki Hidden Strategy
            if price < 250 and currency == "INR":
                print("   [JARVIS TIP]: Yeh stock aapke budget (₹500-1000) mein fit hai!")
            print("-" * 30)
        except:
            print(f"⚠️ {ticker} ka data fetch nahi ho paya.")

if __name__ == "__main__":
    load_future_gems()
