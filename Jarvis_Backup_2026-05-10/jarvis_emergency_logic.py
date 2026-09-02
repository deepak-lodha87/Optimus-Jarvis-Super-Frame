import yfinance as yf
import time
from datetime import datetime
from peewee import *

# Database Setup (Jarvis ki Memory)
db = SqliteDatabase('jarvis_memory.db')

class TradeRecord(Model):
    timestamp = DateTimeField(default=datetime.now)
    ticker = CharField()
    action = CharField()
    price = FloatField()
    balance_after = FloatField()

    class Meta:
        database = db

db.connect()
db.create_tables([TradeRecord])

# Jarvis Settings
current_balance = 1000.0  # Aapka starting amount

def execute_trade(ticker, action, price):
    global current_balance
    if action == "BUY":
        current_balance -= price
    elif action == "SELL":
        current_balance += price
    
    # Save to Database (Memory)
    TradeRecord.create(
        ticker=ticker,
        action=action,
        price=price,
        balance_after=current_balance
    )
    print(f"\n[JARVIS MEMORY] {action} {ticker} at {price:.2f}. Balance: {current_balance:.2f}")

def high_probability_logic(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history(period="1d", interval="1m")
    if data.empty: return

    cp = data['Close'].iloc[-1]
    avg_price = data['Close'].mean()

    # ZERO LOSS STRATEGY: Sirf tab jab price 0.5% niche ho average se
    if cp < avg_price * 0.995:
        execute_trade(ticker, "BUY", cp)
    elif cp > avg_price * 1.005:
        execute_trade(ticker, "SELL", cp)

def daily_summary():
    print("\n--- JARVIS HISTORY REPORT ---")
    for trade in TradeRecord.select().order_by(TradeRecord.timestamp.desc()).limit(5):
        print(f"{trade.timestamp} | {trade.action} {trade.ticker} | Price: {trade.price}")

if __name__ == "__main__":
    print("--- OPTIMUS JARVIS: DATABASE & TRADING ACTIVE ---")
    watchlist = ['ZOMATO.NS', 'PNB.NS', 'IDEA.NS'] # Low price stocks for small budget
    
    try:
        while True:
            now = datetime.now().strftime("%H:%M")
            if "09:15" <= now <= "15:30":
                for stock in watchlist:
                    high_probability_logic(stock)
                    time.sleep(2)
            else:
                print(f"\r[OFF-MARKET] Waiting for 09:15. Last Balance: {current_balance:.2f}", end="")
            
            time.sleep(60)
    except KeyboardInterrupt:
        daily_summary()
        print("\n[SYSTEM] Data saved in jarvis_memory.db")
