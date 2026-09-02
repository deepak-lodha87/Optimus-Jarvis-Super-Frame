import yfinance as yf

def find_momentum_stocks():
    print("==================================================")
    print("      JARVIS HYPER-DRIVE: MOMENTUM SCANNER        ")
    print("==================================================")
    
    # उन स्टॉक्स की लिस्ट जो आज 'Action' में हैं
    watch_list = ["TATAMOTORS.NS", "IREDA.NS", "RVNL.NS", "HDFCBANK.NS", "SUZLON.NS"]
    
    for ticker in watch_list:
        try:
            stock = yf.Ticker(ticker)
            hist = stock.history(period="2d")
            
            # पिछले दिन के मुकाबले आज की बढ़त की गणना
            prev_close = hist['Close'][0]
            curr_price = hist['Close'][1]
            change = ((curr_price - prev_close) / prev_close) * 100
            
            status = "🔥 HIGH MOMENTUM" if change > 3 else "💤 STABLE"
            
            print(f"SYMBOL: {ticker} | CHANGE: {change:.2f}% | STATUS: {status}")
            if change > 3:
                print(f"   [JARVIS]: सर, इसमें पैसा बढ़ रहा है। 'Quick Trade' के लिए तैयार रहें।")
            print("-" * 40)
        except:
            continue

if __name__ == "__main__":
    find_momentum_stocks()
