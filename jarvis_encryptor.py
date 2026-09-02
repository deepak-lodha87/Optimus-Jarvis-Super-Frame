import base64
import time

def encrypt_message(message, secret_key):
    # Simulating a simple XOR-based encryption for Termux demo
    encoded_chars = []
    for i in range(len(message)):
        key_c = secret_key[i % len(secret_key)]
        encoded_c = chr(ord(message[i]) ^ ord(key_c))
        encoded_chars.append(encoded_c)
    
    encoded_string = "".join(encoded_chars)
    return base64.urlsafe_b64encode(encoded_string.encode()).decode()

class CryptoLock:
    def __init__(self):
        self.key = "Optimus_Jarvis_99"

    def secure_comm(self, raw_data):
        print(f"\033[1;36m[ORIGINAL]\033[0m Message: {raw_data}")
        time.sleep(1.2)
        
        encrypted = encrypt_message(raw_data, self.key)
        print(f" \033[1;31m[ENCRYPTING]\033[0m Scrambling data with 256-bit logic...")
        time.sleep(1.5)
        
        print(f" \033[1;32m[SECURE]\033[0m Encrypted Output: {encrypted}")
        
        print(f"\n\033[1;35m[VOICE] Deepak... sir, our secrets are now \nwrapped in a digital vault. Even if someone \nintercepts our signal, they will find \nnothing but chaos. Our communication is \nsacred and silent.\033[0m")

if __name__ == "__main__":
    vault = CryptoLock()
    vault.secure_comm("Jarvis, initiate drone flight to Sector-7.")
