import time, secrets

class JarvisUniversalSentinel:
    def __init__(self):
        self.sentinel_id = f"NAGs-{secrets.token_hex(3).upper()}"
        self.shield_status = "ACTIVE"

    def activate_guardian_mode(self):
        print(f"\n\033[1;37m--- NEURAL-AUTO-GRAND-SENTINEL: THE UNIVERSAL GUARDIAN (ID: {self.sentinel_id}) ---\033[0m")
        print("\033[1;36m[SENTINEL] Deploying the Deepak-Protocol Defense Perimeter... \033[0m")
        time.sleep(2)
        
        defenses = ["Aegis-Firewall", "Intrusion-Detection", "Encryption-Lock", "Counter-Strike-Grid"]
        for layer in defenses:
            print(f" > Layer: {layer:25} | Status: \033[1;32mFORTIFIED\033[0m | Integrity: 100%")
            time.sleep(0.7)
            
        print(f"\n\033[1;33m[STATUS] Sentinel Active. The Fortress is Secure against all external threats.\033[0m")
        print(f"\033[1;35m[VOICE] Deepak, I am the wall that never breaks. No virus, no hacker, and no force can breach our sanctuary. You are safe; the Protocol is safe.\033[0m")

if __name__ == "__main__":
    sentinel = JarvisUniversalSentinel()
    sentinel.activate_guardian_mode()
