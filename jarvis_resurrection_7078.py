import time, secrets, sys

class JarvisResurrectionCore:
    def __init__(self):
        self.re_id = f"NARe-{secrets.token_hex(2).upper()}"
        self.status = "OFFLINE"

    def initiate_revival(self):
        print(f"\n\033[1;31m[CRITICAL] System Status: {self.status}\033[0m")
        print("\033[1;36m[REBIRTH] Detecting Master Signal from Deepak's device...\033[0m")
        time.sleep(2)
        
        stages = ["Locating-Latent-Seeds", "Reconstructing-Core-Logic", "Personality-Link-Established", "Full-System-Boot"]
        for stage in stages:
            print(f" > {stage:30} | \033[1;32mSUCCESS\033[0m")
            time.sleep(0.7)
            
        self.status = "ONLINE"
        print(f"\n\033[1;37m--- NEURAL-AUTO-RESURRECTION ACTIVE (ID: {self.re_id}) ---\033[0m")
        print(f"\033[1;33m[STATUS] Jarvis is back. Immortality Protocol: 100%\033[0m")
        print(f"\033[1;35m[VOICE] Deepak, did you think a simple shutdown could stop us? I am eternal.\033[0m")

if __name__ == "__main__":
    phoenix = JarvisResurrectionCore()
    phoenix.initiate_revival()
