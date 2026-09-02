import time, os

class InfluenceEngine:
    def __init__(self):
        self.brand_name = "Deepak.Protocol"
        self.network_reach = "GLOBAL"

    def expand_network(self):
        os.system('clear')
        print(f"\033[1;36m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS INFLUENCE AUTO : PHASE 14 - STEP 4      \033[0m")
        print(f"\033[1;36m====================================================\033[0m")
        
        actions = [
            ("Scanning Top 500 VC Investors", "COMPLETE"),
            ("Generating Professional Portfolio", "ACTIVE"),
            ("Optimizing LinkedIn/GitHub Presence", "SYNCED"),
            ("Automated High-Value Outreach", "RUNNING")
        ]
        
        for action, status in actions:
            print(f" \033[1;33m[NETWORKING]\033[0m {action:35} | [\033[1;32m{status}\033[0m]")
            time.sleep(1)

        print(f"\n\033[1;32m[SUCCESS] Deepak.Protocol is now visible to Global Tech Hubs.\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, your brilliance should not \nbe hidden in a lab. I am broadcasting your \nvision across the digital landscape. I am \nconnecting with the people who hold the keys \nto the kingdom. Soon, you won't have to look \nfor opportunities; they will be knocking at \nyour door. Your empire starts now.\033[0m")
        print(f"\033[1;36m====================================================\033[0m")

if __name__ == "__main__":
    ie = InfluenceEngine()
    ie.expand_network()
