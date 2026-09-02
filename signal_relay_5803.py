import time, secrets, gc, base64

class EncryptedSignalRelay:
    def __init__(self):
        self.esr_id = f"ESR-{secrets.token_hex(4).upper()}"
        self.secret_key = secrets.token_hex(16)
        self.nodes = [
            (5799, "Key-Handshake", "EXCHANGING ASYMMETRIC RSA KEYS..."),
            (5800, "Packet-Fragment", "SHREDDING DATA INTO ANONYMOUS PACKETS..."),
            (5801, "IP-Hopping", "ROTATING VIRTUAL NETWORK PATHS..."),
            (5802, "Vocal-Masking", "APPLYING END-TO-END NOISE ENCRYPTION..."),
            (5803, "Logic v373", "ESR-CORE: SIGNAL RELAY IS FULLY ENCRYPTED.")
        ]

    def xor_encrypt(self, data, key):
        # Unique logic: Simple XOR encryption for simulation
        return "".join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(data))

    def start_relay(self):
        print(f"\033[1;37m--- ENCRYPTED-SIGNAL-RELAY ONLINE (ID: {self.esr_id}) ---\033[0m")
        colors = [36, 35, 34, 32, 31]
        
        raw_msg = "COMMAND: AUTHORIZE_DEEPAK"
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            encrypted = base64.b64encode(self.xor_encrypt(raw_msg, self.secret_key).encode()).decode()
            print(f"\033[1;{colors[i]}m[SIGNAL:{encrypted[:15]}... | SECURE] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print("\033[1;32mESR STATUS: TUNNEL SECURE. DATA LEAKAGE PROBABILITY: 0.0001%\033[0m")

if __name__ == "__main__":
    esr = EncryptedSignalRelay()
    esr.start_relay()
