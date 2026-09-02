import time

class ProcurementManager:
    def __init__(self):
        self.requirement = "Brushless Motor - 2300KV"
        self.vendors = [
            {"name": "Global_Robotics", "price": 1200, "rating": 4.5, "delivery": "3 Days"},
            {"name": "Local_Tech_Store", "price": 1500, "rating": 4.8, "delivery": "1 Day"},
            {"name": "Import_Hub", "price": 950, "rating": 3.9, "delivery": "15 Days"}
        ]

    def analyze_market(self):
        print(f"\033[1;36m[PROCUREMENT]\033[0m Searching for: {self.requirement}...")
        time.sleep(1.5)
        
        # Logic: Find best balance of price and rating
        best_deal = min(self.vendors, key=lambda x: x['price'] / x['rating'])
        
        print(f" \033[1;32m[BEST DEAL FOUND]\033[0m Vendor: {best_deal['name']}")
        print(f" \033[1;37m[DETAILS]\033[0m Price: ₹{best_deal['price']} | Rating: {best_deal['rating']}★")
        print(f" \033[1;33m[ADVICE]\033[0m This option offers the best value-to-performance ratio.")
        
        print(f"\n\033[1;35m[VOICE] Deepak... sir, I have scanned the \nmarket. Why spend more when we can \nspend smart? I've found the optimal \ncomponents for our next upgrade. Your \nbudget is safe, and our quality is \nassured. Shall I track the prices?\033[0m")

if __name__ == "__main__":
    buyer = ProcurementManager()
    buyer.analyze_market()
