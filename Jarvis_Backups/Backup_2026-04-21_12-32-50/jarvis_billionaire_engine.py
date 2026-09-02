import yfinance as yf

class JarvisGlobalAcquisition:
    def __init__(self):
        print("==================================================")
        print("      JARVIS: GLOBAL ACQUISITION & TAKEOVER       ")
        print("==================================================")

    def analyze_target(self, ticker):
        """कंपनी का मालिकाना हक पाने का पूरा विश्लेषण"""
        try:
            company = yf.Ticker(ticker)
            info = company.info
            name = info.get('longName', ticker)
            mkt_cap = info.get('marketCap', 0)
            currency = info.get('currency', 'USD')

            print(f"\nTARGET: {name} ({ticker})")
            print(f"MARKET VALUE: {mkt_cap / 1e9:.2f} Billion {currency}")
            
            # मालिकाना हक (51% Shares) के लिए जरूरी राशि
            takeover_51 = (mkt_cap * 0.51) / 1e9
            print(f"OWNERSHIP COST (51%): {takeover_51:.2f} Billion {currency}")
            
            # जार्विस की खुफिया राय (Is it worth it?)
            pe_ratio = info.get('trailingPE', 0)
            if pe_ratio < 20 and pe_ratio > 0:
                print("[JARVIS ADVICE]: यह कंपनी सस्ती है। 'Hostile Takeover' के लिए सही समय है।")
            else:
                print("[JARVIS ADVICE]: कंपनी अभी महंगी है। मार्केट क्रैश का इंतज़ार करें।")
            print("-" * 40)
            
        except Exception as e:
            print(f"Data Error: {e}")

# जार्विस को एक्टिव करना (जैसे: Apple या Reliance)
# engine = JarvisGlobalAcquisition()
# engine.analyze_target('RELIANCE.NS')
# engine.analyze_target('TSLA')
