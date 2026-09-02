import yfinance as yf
import pandas as pd

class JarvisFinance:
    def __init__(self):
        self.risk_limit = 0.02 # 2% रिस्क फिक्स
        print("[JARVIS] यूनिवर्सल स्टॉक इंटेलिजेंस एक्टिवेटेड...")

    def scan_market(self, ticker):
        """दुनिया के किसी भी स्टॉक का पूरा कच्चा-चिट्ठा निकालना"""
        try:
            stock = yf.Ticker(ticker)
            info = stock.info
            
            print(f"\n--- {info.get('longName', ticker)} का रिपोर्ट कार्ड ---")
            print(f"Sector: {info.get('sector')}")
            print(f"Business: {info.get('longBusinessSummary')[:200]}...")
            print(f"Current Price: {info.get('currentPrice')} {info.get('currency')}")
            
            # जार्विस का फैसला
            recommendation = info.get('recommendationKey')
            print(f"[JARVIS DECISION]: इस स्टॉक पर मेरी राय '{recommendation.upper()}' है।")
            
        except Exception as e:
            print(f"डेटा फेच करने में एरर: {e}")

# जार्विस को एक्टिव करना
brain = JarvisFinance()
# उदाहरण: Apple (AAPL) या Reliance (RELIANCE.NS)
# brain.scan_market('AAPL') 
