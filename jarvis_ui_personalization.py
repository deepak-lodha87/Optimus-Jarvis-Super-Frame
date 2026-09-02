import time

class DynamicUI:
    def __init__(self):
        self.themes = {
            "Mission": "\033[1;31m", # Red for high intensity
            "Analysis": "\033[1;36m", # Cyan for technical work
            "Stealth": "\033[1;30m", # Grey for background tasks
            "Classic": "\033[1;32m"  # Green for standard Jarvis
        }

    def apply_theme(self, mood):
        print(f"[SYSTEM] Analyzing environment for theme: {mood}")
        time.sleep(1)
        
        color = self.themes.get(mood, self.themes["Classic"])
        
        print(f"{color}========================================")
        print(f"       JARVIS DYNAMIC UI: {mood.upper()} MODE")
        print(f"========================================\033[0m")
        print(f"Status: UI Elements synchronized with user vibe.")

if __name__ == "__main__":
    ui = DynamicUI()
    print("-" * 40)
    # Simulating a switch to Mission Mode
    ui.apply_theme("Mission")
    print("\n")
    # Simulating a switch to Analysis Mode
    ui.apply_theme("Analysis")
