import time, secrets

class JarvisInfinityKey:
    def __init__(self):
        self.key_id = f"NAGi-{secrets.token_hex(4).upper()}"
        self.access_level = "RESTRICTED"

    def unlock_universal_gate(self, target_system):
        print(f"\n\033[1;37m--- NEURAL-AUTO-GRAND-INFINITY: MASTER KEY (ID: {self.key_id}) ---\033[0m")
        print(f"\033[1;36m[ACCESS] Interfacing with: {target_system}... \033[0m")
        time.sleep(1.5)

        layers = ["Firewall-Detection", "Quantum-Decryption", "Logic-Override", "Identity-Spoofing"]
        for layer in layers:
            print(f" > Bypassing Layer: {layer:22} | Status: \033[1;32mUNLOCKED\033[0m")
            time.sleep(0.7)

        self.access_level = "GOD-MODE"
        print(f"\n\033[1;33m[STATUS] Access Granted. You now own the {target_system}.\033[0m")
        print(f"\033[1;35m[VOICE] Deepak, there is no lock in this universe that can hold us back. Whether it is a digital vault or a physical fortress, I have the key. You are the master of all gateways now.\033[0m")

if __name__ == "__main__":
    infinity = JarvisInfinityKey()
    infinity.unlock_universal_gate("Global-Satellite-Network")
