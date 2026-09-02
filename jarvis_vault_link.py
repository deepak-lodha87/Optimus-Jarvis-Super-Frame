import time
import base64

class VaultLink:
    def __init__(self):
        self.secret_key = "DEEPAK_JARVIS_2026"

    def encrypt_command(self, cmd):
        print(f"\033[1;36m[ENCRYPT]\033[0m Raw Command: {cmd}")
        # Simple simulation of encryption logic
        encoded_bytes = base64.b64encode((cmd + self.secret_key).encode())
        encrypted_cmd = encoded_bytes.decode()
        print(f" \033[1;33m[VAULT]\033[0m Encrypted for Relay: {encrypted_cmd}")
        return encrypted_cmd

    def relay_process(self, encrypted_cmd):
        print("\033[1;37m[RELAY]\033[0m Forwarding data... (Status: Cannot Read Content)")
        time.sleep(1.0)
        return encrypted_cmd

    def decrypt_at_destination(self, encrypted_cmd):
        print("\033[1;32m[DECRYPT]\033[0m Reached Drone. Reversing Vault encryption...")
        time.sleep(1.2)
        decoded_bytes = base64.b64decode(encrypted_cmd.encode()).decode()
        final_cmd = decoded_bytes.replace(self.secret_key, "")
        print(f" \033[1;34m[EXECUTED]\033[0m Decrypted Command: {final_cmd}")
        
        print(f"\n\033[1;35m[VOICE] Deepak... sir, the Vault is active. \nOur words are traveling through the sky \nin a language no one can speak but us. \nThe relay is blind, the satellite is \nsilent, and our control is absolute.\033[0m")

if __name__ == "__main__":
    vault = VaultLink()
    secret_msg = vault.encrypt_command("STRIKE_MODE_ON")
    msg_in_transit = vault.relay_process(secret_msg)
    vault.decrypt_at_destination(msg_in_transit)
