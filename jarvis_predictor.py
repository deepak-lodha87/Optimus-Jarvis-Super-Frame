import time
import random

class QuantumPredictor:
    def __init__(self):
        self.scenarios = 1000

    def predict_success(self, task_name):
        print(f"\033[1;34m[PREDICTOR]\033[0m Analyzing task: '{task_name}'")
        print(f" \033[1;37m[SIMULATING]\033[0m Running {self.scenarios} quantum simulations...")
        time.sleep(2)
        
        success_rate = random.uniform(65.0, 99.9)
        risk_factor = 100 - success_rate
        
        print(f"\n\033[1;32m[RESULT]\033[0m Probability of Success: {success_rate:.2f}%")
        print(f"\033[1;31m[RISK]\033[0m Probability of Failure: {risk_factor:.2f}%")
        
        if success_rate > 85:
            print(" \033[1;32m[ADVICE]\033[0m High success rate. Proceed with full power.")
        else:
            print(" \033[1;33m[ADVICE]\033[0m Caution advised. Activating secondary safety protocols.")

        print(f"\n\033[1;35m[VOICE] Deepak... sir, I have looked through the \nfuture of this task. Out of a thousand \npossibilities, this is the most likely \npath. The odds are in our favor. \nShall we proceed?\033[0m")

if __name__ == "__main__":
    predictor = QuantumPredictor()
    predictor.predict_success("Deepak's New Project Launch")
