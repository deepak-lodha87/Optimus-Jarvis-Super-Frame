import time
import random

class OptimusJarvisArmor:
    def __init__(self):
        self.user = "Deepak"
        self.phase_14 = "3014 (Nano-Suit Blueprints)"
        self.phase_15 = "3015 (Strategic HUD Active)"
        self.suit_status = "STARK-FRAME v1.0"

    def load_blueprints(self):
        print(f"\033[1;35m>> PHASE {self.phase_14}: LOADING ADVANCED SCHEMATICS <<\033[0m")
        blueprints = ["Spider-Man Suit", "Iron Man Mark-85", "Stealth Drone Frame"]
        for bp in blueprints:
            print(f"[LOADING] Synchronizing {bp} details...")
            time.sleep(0.5)
        print("\033[1;32m[SUCCESS] Blueprints Integrated into Local Memory.\033[0m")

    def activate_hud(self):
        print(f"\n\033[1;36m>> PHASE {self.phase_15}: PROJECTING STRATEGIC HUD <<\033[0m")
        time.sleep(1)
        # Simulating HUD Data Overlays
        print("\033[1;34m--------------------------------------------------")
        print(f"| USER: {self.user}             | SUIT: {self.suit_status} |")
        print("| POWER: 98.4%             | OXYGEN: STABLE      |")
        print("| RADAR: 0 Threats Detect  | TEMP: 37.2 C        |")
        print("--------------------------------------------------\033[0m")
        print("\033[1;32m[STATUS] HUD Overlay synchronized with Mobile Interface.\033[0m")

    def execute(self):
        print(f"\033[1;32m>> SYSTEM READY. WAKE UP, ARCHITECT DEEPAK. <<\033[0m")
        self.load_blueprints()
        self.activate_hud()

if __name__ == "__main__":
    jarvis = OptimusJarvisArmor()
    jarvis.execute()
