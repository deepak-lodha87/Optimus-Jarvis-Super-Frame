import time
import random

class NeuralCombat:
    def __init__(self):
        self.user = "Deepak"
        self.phase_27 = "3027 (Neural Linkage)"
        self.phase_28 = "3028 (Combat Maneuvers)"
        self.link_stability = 0.0

    def sync_neural_link(self):
        print(f"\033[1;35m>> PHASE {self.phase_27}: ESTABLISHING BRAIN-COMPUTER INTERFACE <<\033[0m")
        time.sleep(1)
        self.link_stability = round(random.uniform(95.0, 99.8), 2)
        print(f"\033[1;34m[LINK] Neural Sync Stability: {self.link_stability}%")
        print("\033[1;32m[SUCCESS] Neural Commands Synchronized with Master Core.\033[0m")

    def execute_countermeasures(self):
        print(f"\n\033[1;36m>> PHASE {self.phase_28}: CALCULATING EVASIVE MANEUVERS <<\033[0m")
        time.sleep(1)
        actions = ["Deploy Flare", "Shield Reinforcement", "Stealth Cloaking"]
        selected = random.choice(actions)
        print(f"\033[1;31m[ACTION] Target firing detected! Executing: {selected}\033[0m")
        print("\033[1;32m[STATUS] Threat Neutralized. Perimeter Secure.\033[0m")

    def run(self):
        print(f"\033[1;32m>> SYSTEM ONLINE: ARCHITECT DEEPAK, WE ARE IN SYNC. <<\033[0m")
        self.sync_neural_link()
        self.execute_countermeasures()

if __name__ == "__main__":
    brain_frame = NeuralCombat()
    brain_frame.run()
