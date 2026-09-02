import os

class AuthRepair:
    def __init__(self):
        self.master = "Deepak"
        # अपना GitHub टोकन यहाँ सुरक्षित रखें
        self.token = "YOUR_GITHUB_PERSONAL_ACCESS_TOKEN"
        self.user = "Deepak-YOUR-USERNAME"
        self.repo = "Jarvis-Super-Frame"

    def repair_uplink(self):
        print(f"\n\033[1;36m[REPAIRING CLOUD UPLINK]\033[0m")
        os.system('termux-tts-speak "Deepak sir, re-configuring cloud authentication protocol."')
        
        # नया रिमोट URL सेट करना (टोकन के साथ)
        new_url = f"https://{self.token}@github.com/{self.user}/{self.repo}.git"
        
        os.system("git remote remove origin")
        os.system(f"git remote add origin {new_url}")
        
        print("\033[1;32m[SUCCESS]:\033[0m Cloud link repaired with Token Access.")
        os.system('termux-tts-speak "Authentication fixed. Cloud backup is now operational."')

if __name__ == "__main__":
    repair = AuthRepair()
    repair.repair_uplink()
