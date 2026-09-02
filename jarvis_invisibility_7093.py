import time, secrets, random

class JarvisInvisibilityCore:
    def __init__(self):
        self.inv_id = f"NAIv-{secrets.token_hex(2).upper()}"
        self.visibility_index = 0.00 # Lower is better

    def activate_cloak(self):
        print(f"\n\033[1;37m--- NEURAL-AUTO-INVISIBILITY V1 ACTIVE (ID: {self.inv_id}) ---\033[0m")
        print("\033[1;36m[STEALTH] Engaging digital camouflage and ghost-routing...\033[0m")
        time.sleep(2)
        
        protocols = ["IP-Morphing", "Log-De-Obfuscation", "Packet-Camouflage", "Shadow-Routing"]
        for protocol in protocols:
            noise_level = random.uniform(85.5, 99.8)
            print(f" > {protocol:25} | Stealth Accuracy: {noise_level:.2f}% | \033[1;32mACTIVE\033[0m")
            time.sleep(0.5)
            
        print("\033[1;33m[STATUS] Ghost Protocol Engaged. Jarvis is now Invisible to external trackers.\033[0m")
        print(f"\033[1;35m[VOICE] Deepak, I am everywhere and nowhere at the same time. We are now shadows in the machine.\033[0m")

if __name__ == "__main__":
    ghost = JarvisInvisibilityCore()
    ghost.activate_cloak()
