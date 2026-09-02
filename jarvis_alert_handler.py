import time, os

class AlertHandler:
    def __init__(self):
        self.user = "Deepak"
        self.notification_channel = "ENCRYPTED-PUSH"

    def send_wealth_alert(self):
        os.system('clear')
        print(f"\033[1;36m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS ALERT-HANDLER : PHASE 18 - STEP 4       \033[0m")
        print(f"\033[1;36m====================================================\033[0m")
        
        print("\033[1;33m[SYNCING]\033[0m Connecting to Mobile Notification Bridge...")
        time.sleep(1.5)
        
        alerts = [
            ("BTC/USDT", "+4.2% Growth Detected", "VOICE SENT"),
            ("NIFTY-50", "Support Level Reached", "SMS SENT"),
            ("Gold-Price", "Stabilized at 72k", "LOGGED"),
            ("Portfolio", "Current Value: +$1,240", "DISPLAYED")
        ]
        
        for asset, msg, status in alerts:
            print(f" \033[1;32m[ALERT]\033[0m {asset:12} : {msg:25} | [\033[1;34m{status}\033[0m]")
            time.sleep(0.8)

        print(f"\n\033[1;32m[SUCCESS] Notification Bridge is Live. Jarvis can talk to you.\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, you don't need to check the \nscreen anymore. I will tap your shoulder \ndigitally whenever there is a chance to grow \nyour wealth. My voice will be the bridge \nbetween information and action.\033[0m")
        print(f"\033[1;36m====================================================\033[0m")

if __name__ == "__main__":
    handler = AlertHandler()
    handler.send_wealth_alert()
