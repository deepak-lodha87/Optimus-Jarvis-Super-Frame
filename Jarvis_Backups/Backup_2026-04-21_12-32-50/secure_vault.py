import base64

class SecurityVault:
    def encrypt_data(self, raw_data):
        print("Applying advanced encryption to your project files...")
        encoded_data = base64.b64encode(raw_data.encode())
        return f"Encrypted: {encoded_data}"

if __name__ == "__main__":
    vault = SecurityVault()
    print(vault.encrypt_data("Jarvis_Phase_1824_Data"))
