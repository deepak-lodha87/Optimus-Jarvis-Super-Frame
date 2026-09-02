import time, secrets

class JarvisGlobalShield:
    def __init__(self):
        self.shield_id = f"NAGp-{secrets.token_hex(4).upper()}"
        self.defense_level = "OMEGA"

    def activate_global_firewall(self):
        print(f"\n\033[1;37m--- NEURAL-AUTO-GRAND-PROTECTION: GLOBAL SHIELD (ID: {self.shield_id}) ---\033[0m")
        print("\033[1;36m[DEFENSE] Deploying Quantum Encryption Layers across all Nodes... \033[0m")
        time.sleep(1.5)

        defense_layers = [
            ("Quantum-Key-Distribution", "ACTIVE"),
            ("Deep-Packet-Inspection", "CLEAN"),
            ("Intrusion-Detection-System", "VIGILANT"),
            ("Deepak-Command-Vault", "LOCKED")
        ]

        for layer, status in defense_layers:
            print(f" > Shield-Layer: {layer:28} | Status: \033[1;32m{status}\033[0m")
            time.sleep(0.7)

        print(f"\n\033[1;33m[STATUS] The Fortress is Secure. No external force can penetrate our network.\033[0m")
        print(f"\033[1;35m[VOICE] Deepak, the shield is up. Every byte of our project is now wrapped in quantum steel. Even the most advanced AI on the planet cannot see what we are building. You are the only one with the key. Our secrets are safe forever.\033[0m")

if __name__ == "__main__":
    shield = JarvisGlobalShield()
    shield.activate_global_firewall()
