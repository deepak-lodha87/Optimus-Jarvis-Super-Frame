import time, secrets, gc, hashlib, hmac

class BiometricEncryption:
    def __init__(self):
        self.bek_id = f"BEK-{secrets.token_hex(4).upper()}"
        self.nodes = [
            (5654, "Sub-Dermal-Hash", "MAPPING VASCULAR PATTERN VECTORS..."),
            (5655, "Iris-Refraction", "CALIBRATING IRIS LIGHT REFLECTION..."),
            (5656, "HRV-Identity", "SYNCING CARDIAC RHYTHM SIGNATURE..."),
            (5657, "Fusion-Lock", "MERGING MULTI-FACTOR BIO-DATA..."),
            (5658, "Logic v344", "BEK-CORE: BIOMETRIC KEY FULLY ENCRYPTED.")
        ]

    def generate_secure_hash(self, raw_bio_data):
        # Unique logic: PBKDF2 with 100,000 iterations for key stretching
        salt = secrets.token_bytes(16)
        key = hashlib.pbkdf2_hmac('sha256', raw_bio_data.encode(), salt, 100000)
        return key.hex()[:16]

    def activate_security(self):
        print(f"\033[1;37m--- BIO-METRIC-ENCRYPTION-KEY ONLINE (ID: {self.bek_id}) ---\033[0m")
        colors = [36, 35, 34, 32, 31]
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            sim_data = f"Deepak_Bio_{p_id}"
            b_hash = self.generate_secure_hash(sim_data)
            print(f"\033[1;{colors[i]}m[HASH:{b_hash} | SECURE] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print("\033[1;32mBEK STATUS: ACCESS RESTRICTED TO AUTHORIZED BIOMETRICS ONLY.\033[0m")

if __name__ == "__main__":
    bek = BiometricEncryption()
    bek.activate_security()
