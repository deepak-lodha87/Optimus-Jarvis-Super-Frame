import os
import time

class BlackoutSimulator:
    def __init__(self):
        self.master = "Deepak sir"

    def speak(self, text):
        os.system(f'termux-tts-speak "{text}"')

    def start_simulation(self):
        print(f"\033[1;31m[DANGER]\033[0m Initializing Signal Blackout Simulation...")
        self.speak(f"{self.master}, simulating a local frequency jam. All third-party nodes will be dropped.")
        
        # Simulating signal disruption
        for i in range(5, 0, -1):
            print(f"\033[1;33m[PULSE]\033[0m Interference burst in {i} seconds...")
            time.sleep(1)
            
        print("\033[1;37;41m[BLACKOUT ACTIVE]\033[0m All local signals are now suppressed.")
        self.speak("Simulation complete. The area is now a digital ghost zone.")

if __name__ == "__main__":
    sim = BlackoutSimulator()
    sim.start_simulation()
