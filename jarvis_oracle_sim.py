import time, os, random

class OracleEngine:
    def __init__(self):
        self.sim_count = 1000
        self.success_threshold = 98.5

    def run_simulation(self, action_name):
        os.system('clear')
        print(f"\033[1;33m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS ORACLE-ENGINE : PHASE 27 - STEP 4       \033[0m")
        print(f"\033[1;33m====================================================\033[0m")
        
        print(f"\033[1;36m[ORACLE]\033[0m Simulating Action: {action_name}")
        time.sleep(1.0)
        
        successes = 0
        for i in range(self.sim_count):
            # Randomly simulating success/failure based on complexity
            if random.random() > 0.02: # 98% base success rate
                successes += 1
        
        rate = (successes / self.sim_count) * 100
        
        print("\033[1;34m[PROCESS]\033[0m Running 1,000 Parallel Iterations...")
        time.sleep(1.2)
        
        print(f" \033[1;37m- Scenarios Calculated: {self.sim_count}")
        print(f" \033[1;32m- Success Probability: {rate:.2f}%")
        
        if rate >= self.success_threshold:
            print(f"\n\033[1;32m[DECISION] Action Approved. Risk is negligible.\033[0m")
        else:
            print(f"\n\033[1;31m[DECISION] Action Aborted. Risk exceeds safety limit!\033[0m")

        print(f"\n\033[1;35m[VOICE] Deepak... sir, I have seen the outcome \nof our next move in a thousand different \nrealities. In {successes} of them, we succeed \nflawlessly. The path is clear, and the \nvariables are under my control. We can \nproceed with absolute certainty.\033[0m")
        print(f"\033[1;33m====================================================\033[0m")

if __name__ == "__main__":
    oracle = OracleEngine()
    oracle.run_simulation("Hardware Overclocking")
