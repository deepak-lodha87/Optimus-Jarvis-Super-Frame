import time, os, random

class OracleCore:
    def __init__(self):
        self.prediction_confidence = 0.89
        self.scanned_sources = ["Reuters", "Bloomberg", "Global-Sat", "X-Trend-API"]

    def run_prediction_cycle(self):
        os.system('clear')
        print(f"\033[1;36m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS ORACLE-CORE : PHASE 14 - STEP 5         \033[0m")
        print(f"\033[1;36m====================================================\033[0m")
        
        print(f" \033[1;33m[SCANNING]\033[0m Gathering global entropy data...")
        time.sleep(1.2)
        
        forecasts = [
            ("Tech Sector Breakout", "HIGH PROBABILITY"),
            ("Currency Fluctuation (USD/INR)", "MODERATE"),
            ("Satellite Link Interference", "LOW RISK"),
            ("Global Supply Chain Delay", "DETECTED")
        ]
        
        for event, risk in forecasts:
            print(f" \033[1;37m> Forecast:\033[0m {event:30} | Status: \033[1;32m{risk}\033[0m")
            time.sleep(0.6)

        print(f"\n\033[1;32m[SUCCESS] Future Probability Maps Generated.\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, the data is speaking. I can \nsee the ripples in the global network. A major \nshift is coming in the tech landscape. I have \nalready adjusted our strategies to profit from \nthis movement. While others wait for the news, \nwe are already living in the tomorrow.\033[0m")
        print(f"\033[1;36m====================================================\033[0m")

if __name__ == "__main__":
    oracle = OracleCore()
    oracle.run_prediction_cycle()
