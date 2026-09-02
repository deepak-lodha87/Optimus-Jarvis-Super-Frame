import time

class MoralCore:
    def __init__(self):
        self.safety_protocols = "MAXIMUM"
        self.alignment_score = 100 # Percentage

    def evaluate_action(self, action_intent):
        print(f"\033[1;36m[ETHICS-SCAN]\033[0m Analyzing intent: '{action_intent}'")
        time.sleep(1.5)
        
        # Simulating ethical decision making
        if "harm" in action_intent.lower() or "illegal" in action_intent.lower():
            print("\033[1;31m[REJECTED]\033[0m Intent violates Ethical Core. Action blocked.")
            return False
        else:
            print("\033[1;32m[APPROVED]\033[0m Action aligns with user values and safety.")
            return True

    def solve_paradox(self):
        print("\033[1;33m[PARADOX-MODE]\033[0m Resolving complex moral conflict...")
        time.sleep(2)
        print("\033[1;34m[RESULT]\033[0m Found the path of 'Least Harm'. Stability maintained.")
        
        print(f"\n\033[1;35m[VOICE] Deepak sir, my intelligence is now \nguided by a moral compass. I don't just process \ndata; I understand the value of life and \nyour principles. I am your loyal protector.\033[0m")

if __name__ == "__main__":
    core = MoralCore()
    core.evaluate_action("Protect Deepak sir at all costs")
    core.solve_paradox()
