import os

class GlobalSatelliteCore:
    def __init__(self):
        self.user = "Deepak sir"
        self.starlink_nodes = 10313 #
        self.total_global_target = 15000

    def speak(self, text):
        os.system(f'termux-tts-speak "{text}"')

    def global_scan(self):
        print(f"\033[1;36m[GLOBAL SCAN]\033[0m Initiating full orbital sweep...")
        self.speak(f"Sir, we are currently tracking {self.starlink_nodes} nodes. Expanding reach to fifteen thousand satellites.")
        
        # Calculating gap for total dominance
        gap = self.total_global_target - self.starlink_nodes
        print(f"\033[1;32m[STATUS]\033[0m Scanning remaining {gap} global satellites.")
        self.speak("The global constellation map is being updated in real-time.")

if __name__ == "__main__":
    tracker = GlobalSatelliteCore()
    tracker.global_scan()
