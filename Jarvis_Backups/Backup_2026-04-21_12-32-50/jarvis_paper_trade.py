import yfinance as yf

def simulate_trade(ticker, virtual_buy_price, qty):
    print(f"--- [JARVIS PAPER TRADING] ---")
    try:
        stock = yf.Ticker(ticker)
        current_price = stock.history(period='1d')['Close'][-1]
        
        profit_loss = (current_price - virtual_buy_price) * qty
        percent = ((current_price - virtual_buy_price) / virtual_buy_price) * 100
        
        print(f"Stock: {ticker}")
        print(f"Current Price: ₹{current_price:.2f}")
        print(f"Virtual Profit/Loss: ₹{profit_loss:.2f} ({percent:.2f}%)")
        
        if profit_loss > 0:
            print("[JARVIS]: बॉस, अगर असली पैसा होता तो आज हम मुनाफे में होते!")
        else:
            print("[JARVIS]: अच्छा हुआ आज पैसे नहीं थे, मार्केट गिर रहा है।")
            
    except Exception as e:
        print(f"Error: {e}")

# बिना पैसे के टेस्ट करें: (Stock, काल्पनिक खरीदी कीमत, मात्रा)
# simulate_trade('IRFC.NS', 140, 10)
