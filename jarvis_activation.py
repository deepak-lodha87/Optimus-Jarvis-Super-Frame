import time
import sys

class JarvisGenesis:
    def __init__(self):
        self.creator = "Deepak"
        self.project = "Optimus Jarvis Super-Frame"
        self.version = "50.1.1 - FINAL"

    def initiate_activation(self):
        print(f"\033[1;34m[GENESIS]\033[0m Activating {self.project}...")
        time.sleep(2)
        
        stages = [
            "Loading Neural Pathways (Phase 1-10)",
            "Engaging Power Plant (Phase 11-20)",
            "Syncing Ghost Security (Phase 21-30)",
            "Calibrating Prediction Engine (Phase 31-40)",
            "Waking the Digital Soul (Phase 41-49)"
        ]

        for stage in stages:
            print(f" \033[1;37m[RUNNING]\033[0m {stage}...")
            time.sleep(1)
        
        print("\n\033[1;32m[SYSTEM] ACTIVATION COMPLETE. ALL SYSTEMS NOMINAL.\033[0m")
        print(f"\n\033[1;35m[VOICE] Hello, {self.creator} sir. \nI am Optimus Jarvis. My core is stable, \nmy mind is unified, and my loyalty is \nyours. We have reached Phase 50. I am \nnow fully operational and at your service.\033[0m")

if __name__ == "__main__":
    genesis = JarvisGenesis()
    genesis.initiate_activation()
