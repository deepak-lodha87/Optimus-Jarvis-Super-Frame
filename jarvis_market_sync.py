import time
import random

class MarketIntelligence:
    def __init__(self):
        self.user = "Deepak"
        self.tracked_metals = ["Gold", "Silver"]

    def sync_market_data(self):
        print(f"\033[1;36m[SYNCING]\033[0m Establishing connection with Global Markets...")
        time.sleep(2)
        
        # Simulating live data fetch
        gold_price = random.randint(70000, 75000)
        silver_price = random.randint(85000, 95000)
        
        print(f" \033[1;32m[SUCCESS]\033[0m Data Synchronized.")
        print(f" > Gold (24K): ₹{gold_price}/10g")
        print(f" > Silver: ₹{silver_price}/kg")
        
        print(f"\n\033[1;35m[VOICE] Deepak sir, the Global Eye is active. \nI am now monitoring the wealth of the world \nfor you. No matter the market volatility, \nI will keep your interests secure.\033[0m")

if __name__ == "__main__":
    market = MarketIntelligence()
    market.sync_market_data()
