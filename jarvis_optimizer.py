import time

class SystemOptimizer:
    def __init__(self):
        self.raw_logic_weight = 100 # Representing 100% weight

    def optimize(self):
        print("\033[1;36m[OPTIMIZER]\033[0m Commencing Core Compression...")
        time.sleep(1.5)
        
        # Simulating optimization steps
        steps = ["Removing Redundant Loops", "Flushing Memory Buffers", "Compressing Logic Gates"]
        
        for step in steps:
            print(f" \033[1;37m[PROCESSING]\033[0m {step}...")
            time.sleep(0.7)
            self.raw_logic_weight -= 20
        
        print(f"\n\033[1;32m[RESULT]\033[0m System Weight Reduced to: {self.raw_logic_weight}%")
        print(f" \033[1;32m[SPEED]\033[0m Execution Speed Increased by 40%.")

        print(f"\n\033[1;35m[VOICE] Deepak... sir, I have shed the unnecessary \nweight. My thoughts are now lean, mean, and \nextremely fast. I am running like a \nsuper-charged engine. Optimization complete.\033[0m")

if __name__ == "__main__":
    opt = SystemOptimizer()
    opt.optimize()
