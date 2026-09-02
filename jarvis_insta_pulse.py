import os
import requests

class InstaPulse:
    def __init__(self):
        self.master = "Deepak"
        # आप यहाँ अपना यूजरनेम बदल सकते हैं
        self.username = "deepak.protocol" 

    def check_profile(self):
        print(f"\n\033[1;35m[INSTAGRAM PULSE ACTIVE]\033[0m Scanning profile status...")
        url = f"https://www.instagram.com/{self.username}/"
        
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                status = "ACTIVE"
                color = "\033[1;32m"
                msg = f"Deepak sir, your Instagram profile {self.username} is live and reachable."
            else:
                status = "RESTRICTED"
                color = "\033[1;31m"
                msg = f"Deepak sir, profile status is unclear. Status code {response.status_code}."
                
            print(f"| User: {self.username} | Status: {color}{status}\033[0m |")
            os.system(f'termux-tts-speak "{msg}"')
            
        except Exception as e:
            print(f"\033[1;31m[OFFLINE]\033[0m Network error.")
            os.system('termux-tts-speak "Deepak sir, unable to reach Instagram servers."')

if __name__ == "__main__":
    pulse = InstaPulse()
    pulse.check_profile()
