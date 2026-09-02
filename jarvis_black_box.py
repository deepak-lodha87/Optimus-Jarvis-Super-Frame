import os
import base64

class BlackBoxArchive:
    def __init__(self):
        self.vault_path = "jarvis_vault"
        if not os.path.exists(self.vault_path):
            os.makedirs(self.vault_path)

    def secure_data(self, filename, data):
        # Data ko encode karke "Invisible" banana
        encoded_data = base64.b64encode(data.encode())
        with open(f"{self.vault_path}/{filename}.jv", "wb") as f:
            f.write(encoded_data)
        print(f"\033[1;32m[SECURED]\033[0m Data stored in Black-Box: {filename}.jv")

    def retrieve_data(self, filename):
        try:
            with open(f"{self.vault_path}/{filename}.jv", "rb") as f:
                decoded_data = base64.b64decode(f.read()).decode()
                print(f"\033[1;34m[RECOVERED]\033[0m Data: {decoded_data}")
        except FileNotFoundError:
            print("\033[1;31m[ERROR]\033[0m File not found in Sub-Space.")

if __name__ == "__main__":
    box = BlackBoxArchive()
    box.secure_data("Project_Vision", "Deepak sir is the creator of the Super-Frame.")
    box.retrieve_data("Project_Vision")
