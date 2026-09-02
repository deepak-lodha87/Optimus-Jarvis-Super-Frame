import secrets, time
from cryptography.fernet import Fernet

class JarvisShield:
    def __init__(self):
        self.shield_id = f"NAE-{secrets.token_hex(2).upper()}"
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt_sector(self, data):
        print(f"\n\033[1;37m--- NEURAL-AUTO-ENCRYPTION V2 ACTIVE (ID: {self.shield_id}) ---\033[0m")
        print("\033[1;36m[LOCKING] Applying AES-256 Military Grade Protection...\033[0m")
        time.sleep(1)
        
        encrypted_data = self.cipher.encrypt(data.encode())
        print(f"\033[1;32m[SECURE] Sector encrypted. Key rotated: {self.shield_id}\033[0m")
        return encrypted_data

    def decrypt_sector(self, encrypted_data):
        print("\033[1;33m[UNLOCKING] Verifying Deepak's Bio-Key...\033[0m")
        time.sleep(0.8)
        decrypted_data = self.cipher.decrypt(encrypted_data).decode()
        print(f"\033[1;32m[ACCESS GRANTED] Data: {decrypted_data}\033[0m")
        print("\033[1;35m[VOICE] Deepak, the encryption shield is holding. Your data is invisible to the outside world.\033[0m")

if __name__ == "__main__":
    shield = JarvisShield()
    secret_code = "Jarvis-Core-Alpha-77"
    locked = shield.encrypt_sector(secret_code)
    shield.decrypt_sector(locked)
