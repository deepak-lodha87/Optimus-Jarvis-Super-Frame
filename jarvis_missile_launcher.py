import time

class TacticalArsenal:
    def __init__(self):
        self.payload = 12 # Micro-missiles
        self.target_locked = False

    def engage_target(self, target_name):
        print(f"\033[1;31m[LOCKING]\033[0m Scanning for {target_name}...")
        time.sleep(1.5)
        self.target_locked = True
        print(f" \033[1;32m[LOCKED]\033[0m Target {target_name} in range.")
        print(f" \033[1;33m[LAUNCH]\033[0m Firing 2 micro-missiles...")
        self.payload -= 2
        print(f" \033[1;34m[STATUS]\033[0m Remaining Payload: {self.payload}")

if __name__ == "__main__":
    arsenal = TacticalArsenal()
    arsenal.engage_target("Enemy Drone")
