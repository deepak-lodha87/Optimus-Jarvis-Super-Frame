import os
import subprocess

class EcosystemScanner:
    def __init__(self):
        self.master = "Deepak"

    def scan_apps(self):
        print(f"\n\033[1;36m[ECOSYSTEM SCANNER ACTIVE]\033[0m Mapping installed applications...")
        
        try:
            # Termux API से इंस्टॉल किए गए ऐप्स की लिस्ट लेना
            result = subprocess.run(['termux-telephony-deviceinfo'], capture_output=True, text=True)
            # यहाँ हम एक सरल ऐप काउंट कमांड का उपयोग कर रहे हैं जो Termux में उपलब्ध है
            app_list = subprocess.run(['pm', 'list', 'packages'], capture_output=True, text=True)
            
            apps = app_list.stdout.split('\n')
            # खाली लाइन्स को हटाना
            apps = [a for a in apps if a.strip()]
            total_apps = len(apps)
            
            print(f"\033[1;32m[SCAN COMPLETE]:\033[0m Detected {total_apps} software packages.")
            
            msg = f"Deepak sir, I have successfully mapped your mobile ecosystem. You have {total_apps} applications installed."
            os.system(f'termux-tts-speak "{msg}"')
            
        except Exception as e:
            print(f"\033[1;31m[ERROR]:\033[0m Could not access app list. {e}")
            os.system('termux-tts-speak "Deepak sir, application scanning failed due to permission issues."')

if __name__ == "__main__":
    scanner = EcosystemScanner()
    scanner.scan_apps()
