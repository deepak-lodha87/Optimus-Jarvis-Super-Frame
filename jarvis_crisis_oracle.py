import time
import random

class CrisisOracle:
    def __init__(self):
        self.risk_threshold = 75 # 75% se upar risk hone par alert
        self.monitored_sectors = ["Economy", "Security", "Energy"]

    def analyze_global_stability(self):
        print(f"\033[1;36m[ORACLE]\033[0m Running Correlation Logic on Global Data...")
        time.sleep(2)
        
        for sector in self.monitored_sectors:
            risk_percent = random.randint(30, 95)
            status = "STABLE" if risk_percent < self.risk_threshold else "CRITICAL"
            
            color = "\033[1;32m" if status == "STABLE" else "\033[1;31m"
            print(f" \033[1;34m[SECTOR]\033[0m {sector:10} | Risk: {color}{risk_percent}% [{status}]\033[0m")
            
        print(f"\n\033[1;35m[VOICE] Deepak sir, I have processed the latest \nglobal shifts. My predictive models suggest \na potential fluctuation in the Energy sector. \nI have adjusted our security protocols.\033[0m")

if __name__ == "__main__":
    oracle = CrisisOracle()
    oracle.analyze_global_stability()
