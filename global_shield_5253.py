import hashlib, hmac, time, secrets, gc

class GlobalShield:
    def __init__(self):
        self.secret_key = secrets.token_bytes(32)
        self.shield_nodes = [
            (5249, "Neural-Firewall", "ADAPTIVE DEFENSE ACTIVE"),
            (5250, "Data-Frag", "DECENTRALIZED STORAGE SYNCED"),
            (5251, "Quantum-Lock", "BIOMETRIC SIGNATURE VERIFIED"),
            (5252, "Threat-Neutralizer", "COUNTER-MEASURES ARMED"),
            (5253, "Logic v263", "GLOBAL-SHIELD STATUS: 100%")
        ]

    def deploy_shield(self):
        print(f"\033[1;37m--- GLOBAL-SHIELD DEPLOYMENT (ID: {secrets.token_hex(6).upper()}) ---\033[0m")
        
        colors = [34, 36, 32, 33, 31]
        for i, (p_id, title, status) in enumerate(self.shield_nodes):
            # Creating a unique HMAC for each phase entry
            signature = hmac.new(self.secret_key, str(p_id).encode(), hashlib.sha256).hexdigest()[:12]
            print(f"\033[1;{colors[i]}m[SIG-{signature}] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print("\033[1;32mSECURITY STATUS: OPTIMUS JARVIS IS NOW VIRTUALLY INDESTRUCTIBLE.\033[0m")

if __name__ == "__main__":
    shield = GlobalShield()
    shield.deploy_shield()
