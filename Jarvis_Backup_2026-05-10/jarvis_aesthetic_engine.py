import time
import random

class AestheticDesign:
    def __init__(self):
        self.themes = {
            "Combat": "\033[1;31m", # Red
            "Analysis": "\033[1;36m", # Cyan
            "Stealth": "\033[1;30m", # Dark Gray
            "Default": "\033[1;32m"  # Green
        }

    def apply_theme(self, mode):
        color = self.themes.get(mode, self.themes["Default"])
        print(f"{color}[DESIGN] Switching to {mode} Visual Profile...[SYNCED]\033[0m")
        time.sleep(1)
        return color

class VisualFeedback:
    def pulse_effect(self, color_code):
        print(f"{color_code}   >>> SYSTEM HEARTBEAT ACTIVE <<<\033[0m")
        for _ in range(3):
            print(f"{color_code} . \033[0m", end=" ", flush=True)
            time.sleep(0.4)
        print("\n")

if __name__ == "__main__":
    aes = AestheticDesign()
    vis = VisualFeedback()
    
    print("-" * 50)
    print("   JARVIS NEURAL AESTHETIC ENGINE (P3113-14)")
    print("-" * 50)
    
    # Simulating a theme change based on activity
    current_color = aes.apply_theme("Analysis")
    vis.pulse_effect(current_color)
    
    print(f"{current_color}[STATUS] Interface is now optimized for high-level data visualization.\033[0m")
    print("-" * 50)
