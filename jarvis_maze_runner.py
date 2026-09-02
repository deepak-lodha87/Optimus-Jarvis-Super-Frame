import time
import random

class MazeRunner:
    def __init__(self):
        self.destination = "Base_Alpha"
        self.path_blocked = False

    def navigate(self):
        print(f"\033[1;36m[NAVIGATING]\033[0m Target Locked: {self.destination}")
        time.sleep(1.0)
        
        # Simulating a sudden obstacle
        self.path_blocked = random.choice([True, False])
        
        if self.path_blocked:
            print(" \033[1;31m[BLOCKADE]\033[0m Sudden obstacle detected on Main Route!")
            print(" \033[1;33m[RE-ROUTING]\033[0m Calculating alternative coordinates...")
            time.sleep(1.5)
            print(" \033[1;32m[SUCCESS]\033[0m New path found via Sector-7. Distance: +200m.")
        else:
            print(" \033[1;32m[CLEAR]\033[0m Main path is open. Maintaining speed.")

        print(f"\n\033[1;35m[VOICE] Deepak... sir, a wall is just a \ndetour in disguise. I have already \nmapped a new way around the obstacle. \nWe don't stop; we just evolve our \ndirection. The target is still in sight.\033[0m")

if __name__ == "__main__":
    runner = MazeRunner()
    runner.navigate()
