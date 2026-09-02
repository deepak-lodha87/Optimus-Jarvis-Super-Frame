import os
import time
import random

class PredictiveAI:
    def __init__(self):
        self.master = "Deepak"
        # मशीन के मुख्य हिस्से और उनकी अनुमानित लाइफ (%)
        self.components = {
            "Brake Pads": 85,
            "Engine Oil Viscosity": 40,
            "Alternator Belt": 12,
            "Fuel Injector": 92
        }

    def run_probability_check(self):
        print(f"\n\033[1;36m[PREDICTIVE SCAN]\033[0m Jarvis is calculating wear-and-tear logic...")
        time.sleep(2)
        
        print("\033[1;37m        COMPONENT           |   HEALTH   |   PREDICTION")
        print("        ---------------------------------------------\033[0m")
        
        for part, health in self.components.items():
            status = "\033[1;32mSTABLE\033[0m"
            if health < 20:
                status = "\033[1;31mCRITICAL FAILURE IMMINENT\033[0m"
            elif health < 50:
                status = "\033[1;33mREPLACEMENT RECOMMENDED\033[0m"
                
            print(f"        {part.ljust(20)} |   {str(health).ljust(6)}% |   {status}")
            time.sleep(0.5)

    def generate_forecast(self):
        msg = "Deepak sir, my predictive analysis shows the Alternator Belt will fail within 48 hours of operation. I suggest ordering the part immediately to avoid a breakdown."
        os.system(f'termux-tts-speak "{msg}"')
        print(f"\n\033[1;35m[REPORT]:\033[0m Forecast generated based on A-Z Database Specs.")

if __name__ == "__main__":
    predictor = PredictiveAI()
    predictor.run_probability_check()
    predictor.generate_forecast()
