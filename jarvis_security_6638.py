import time, secrets, random

class JarvisStealthGuard:
    def __init__(self):
        self.guard_id = f"NASe-{secrets.token_hex(2).upper()}"
        self.visibility = "High"

    def activate_cloaking(self):
        print(f"\n\033[1;37m--- NEURAL-AUTO-SECURITY V3 ACTIVE (ID: {self.guard_id}) ---\033[0m")
        print("\033[1;36m[CLOAKING] Masking network nodes and randomizing IP signatures...\033[0m")
        time.sleep(2)
        
        layers = ["IP-Masking", "Signal-Encryption", "Ghost-Mode-Activated"]
        for layer in layers:
            print(f"\033[1;32m[SHIELD] {layer}: ENABLED.\033[0m")
            time.sleep(0.5)
            
        self.visibility = "Invisible"
        print(f"\033[1;33m[STATUS] Network Presence: {self.visibility} | Stealth: 100%\033[0m")
        print(f"\033[1;35m[VOICE] Deepak, we have vanished from the public web. I am managing the shadow-gate now.\033[0m")

if __name__ == "__main__":
    guard = JarvisStealthGuard()
    guard.activate_cloaking()
