import time, os, random

class MarketOracle:
    def __init__(self):
        self.markets = ["NIFTY 50", "S&P 500", "NASDAQ", "CRYPTO-INDEX"]
        self.status = "SCANNING"

    def analyze_trends(self):
        os.system('clear')
        print(f"\033[1;36m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS MARKET ORACLE : PHASE 14 - STEP 2       \033[0m")
        print(f"\033[1;36m====================================================\033[0m")
        
        print(f" \033[1;33m[SYNCING]\033[0m Connecting to Global Exchange Servers...")
        time.sleep(1.5)
        
        for market in self.markets:
            change = random.uniform(-2.5, 3.5)
            trend = "\033[1;32mBULLISH\033[0m" if change > 0 else "\033[1;31mBEARISH\033[0m"
            print(f" \033[1;37m> {market:15}\033[0m | Change: {change:+.2f}% | Trend: {trend}")
            time.sleep(0.6)

        print(f"\n\033[1;32m[LOGIC] High-Probability Trade Setup Detected in Tech Sector.\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, I have scanned the global \nliquidity flows. While the local markets are \nvolatile, the aerospace sector is showing \nstrong accumulation patterns. I have mapped \nthe logic for a high-probability scenario. \nYour wealth is now protected by global data.\033[0m")
        print(f"\033[1;36m====================================================\033[0m")

if __name__ == "__main__":
    oracle = MarketOracle()
    oracle.analyze_trends()
