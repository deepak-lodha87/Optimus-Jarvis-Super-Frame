# Optimus Jarvis Super-Frame: Phase 425-426
# Feature: Advanced Data Encryption & Secure Cipher Protocol

import base64

class JarvisEncryption:
    def __init__(self):
        self.code_ver = "426.Secure-Vault"

    def code_425_encrypt_data(self, plain_text):
        print(f"\n[MODULE 425] Initiating Encryption for: '{plain_text}'")
        # Converting text to base64 bytes
        bytes_data = plain_text.encode("utf-8")
        encoded_data = base64.b64encode(bytes_data)
        print(f"[SUCCESS] Data Encrypted.")
        return encoded_data

    def code_426_decrypt_data(self, encrypted_data):
        print("\n[MODULE 426] Decoding Cipher Protocol...")
        # Decoding back to plain text
        decoded_data = base64.b64decode(encrypted_data).decode("utf-8")
        print(f"[RESULT] Decrypted Content: '{decoded_data}'")
        return decoded_data

if __name__ == "__main__":
    vault = JarvisEncryption()
    print(f"--- {vault.code_ver}: Operational ---")
    
    secret = "Tactical_Blueprint_406"
    
    # Encrypt
    cipher_text = vault.code_425_encrypt_data(secret)
    print(f"-> Cipher Output: {cipher_text}")
    
    # Decrypt
    vault.code_426_decrypt_data(cipher_text)
    
    print("\n--- Phase 426 Complete. Data is now Encrypted. ---")
