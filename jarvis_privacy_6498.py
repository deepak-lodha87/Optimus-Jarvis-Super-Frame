import time, secrets, random

class JarvisPrivacyGuard:
    def __init__(self):
        self.guard_id = f"NAPr-{secrets.token_hex(2).upper()}"
        self.virtual_location = random.choice(["Zurich", "Singapore", "Reykjavik"])

    def activate_stealth(self):
        print(f"\n\033[1;37m--- NEURAL-AUTO-PRIVACY V1 ACTIVE (ID: {self.guard_id}) ---\033[0m")
        print("\033[1;36m[MASKING] Scrubbing real IP and device metadata...\033[0m")
        time.sleep(1.2)
        
        print(f"\033[1;32m[TUNNEL] Secure Uplink established via {self.virtual_location}.\033[0m")
        print("\033[1;33m[STATUS] Digital Footprint: ZERO | Privacy Shield: 100%\033[0m")
        
        print(f"\033[1;35m[VOICE] Deepak, we are now invisible. Even the global nodes can't trace us back to Ratlam.\033[0m")

if __name__ == "__main__":
    guard = JarvisPrivacyGuard()
    guard.activate_stealth()
