import time, secrets, random

class GhostMode:
    def __init__(self):
        self.ngm_id = f"GHOST-{secrets.token_hex(2).upper()}"
        self.active_identity = "Original-Deepak"

    def activate_stealth(self):
        print(f"\n\033[1;37m--- NEURAL-GHOST-MODE ONLINE (ID: {self.ngm_id}) ---\033[0m")
        locations = ["USA", "Japan", "Germany", "Iceland", "Singapore"]
        
        for i in range(1, 4):
            new_loc = random.choice(locations)
            print(f"\033[1;33m[SPOOFING] Routing through: {new_loc}...\033[0m")
            time.sleep(0.5)
            self.active_identity = f"Anon-{secrets.token_hex(3)}"
            print(f"\033[1;32m[OK] Identity Masked as: {self.active_identity}\033[0m")

    def strip_metadata(self, filename):
        print(f"\n\033[1;36m[CLEANING] Stripping metadata from {filename}...\033[0m")
        time.sleep(0.8)
        print("\033[1;32m[SUCCESS] Device info, GPS data, and Timestamps removed.\033[0m")

if __name__ == "__main__":
    ghost = GhostMode()
    ghost.activate_stealth()
    # Simulating cleaning an image file like your screenshots
    ghost.strip_metadata("screenshot_1000268504.jpg")
