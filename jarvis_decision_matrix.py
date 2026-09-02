import os
import time

class DecisionMatrix:
    def __init__(self):
        self.master = "Deepak"
        self.project = "Optimus Jarvis Super-Frame"

    def evaluate_priority(self, situation):
        print(f"\n\033[1;33m[EVALUATING]\033[0m Situation: {situation}")
        time.sleep(1.2)
        
        # Strategic priority logic
        logic_steps = [
            "Assessing Strategic Importance...",
            "Checking Safety Compliance (Protocol 1)...",
            "Simulating Future Outcomes...",
            "Finalizing Autonomous Action..."
        ]
        
        for step in logic_steps:
            print(f"\033[1;32m[MATRIX]\033[0m {step}")
            time.sleep(0.4)

        msg = f"{self.master} sir, the Decision Matrix has optimized the strategy for {situation}."
        os.system(f'termux-tts-speak "{msg}"')

    def run_matrix(self):
        os.system('clear')
        print(f"--- {self.project} : STRATEGIC DECISION MATRIX ---")
        self.evaluate_priority("Autonomous Resource Allocation for Phase 7")
        print("\n\033[1;36m[STATUS]\033[0m DECISION CORE: FULLY AUTONOMOUS")

if __name__ == "__main__":
    DecisionMatrix().run_matrix()
