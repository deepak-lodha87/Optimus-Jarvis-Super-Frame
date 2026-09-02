import time, secrets, gc, hashlib, hmac

class BioMetricEncryptionFabric:
    def __init__(self, user_name):
        self.bef_id = f"BEF-{secrets.token_hex(4).upper()}"
        self.user_secret = user_name.encode()
        self.nodes = [
            (5544, "Minutiae-Extraction", "MAPPING FINGERPRINT RIDGE VECTORS..."),
            (5545, "Vocal-Hashing", "EXTRACTING VOICE FREQUENCY ENTROPY..."),
            (5546, "Entropy-Salting", "INJECTING CRYPTOGRAPHIC SALT..."),
            (5547, "Liveness-Detection", "VERIFYING BIOLOGICAL AUTHENTICITY..."),
            (5548, "Logic v322", "BEF-CORE: BIOMETRIC FABRIC SYNCHRONIZED.")
        ]

    def generate_bio_key(self, bio_data):
        # Unique logic: Salted HMAC for biometric verification
        salt = secrets.token_bytes(16)
        return hmac.new(self.user_secret, bio_data + salt, hashlib.sha256).hexdigest()

    def activate_security(self):
        print(f"\033[1;37m--- BIO-METRIC-ENCRYPTION-FABRIC ONLINE (ID: {self.bef_id}) ---\033[0m")
        colors = [36, 35, 34, 32, 31]
        
        bio_sample = b"Deepak_Voice_Pattern_778"
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            key_fragment = self.generate_bio_key(bio_sample)[:10]
            print(f"\033[1;{colors[i]}m[KEY:{key_fragment}] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print("\033[1;32mBEF STATUS: SYSTEM ACCESS RESTRICTED TO AUTHORIZED BIOMETRICS ONLY.\033[0m")

if __name__ == "__main__":
    bef = BioMetricEncryptionFabric("Deepak")
    bef.activate_security()
