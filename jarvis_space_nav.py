import time, os

class JarvisAstroNavigator:
    def __init__(self):
        self.version = "1,000,000+ PHASES"
        self.location = "ORBITAL-SYNC-READY"

    def initiate_space_protocols(self):
        os.system('clear')
        print(f"\033[1;36m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS ASTRO-NAVIGATION : PHASE 8 - STEP 4     \033[0m")
        print(f"\033[1;36m====================================================\033[0m")
        
        astro_checks = [
            ("Pulsar Map Syncing", "MAPPING GALAXY"),
            ("Starhawk Blueprint Load", "STRUCTURAL INTEGRITY OK"),
            ("Vacuum Seal Validation", "PRESSURE STABLE"),
            ("Deepak-Prime Commander-Auth", "ACCESS GRANTED")
        ]
        
        for task, status in astro_checks:
            print(f" \033[1;33m[NAV-SYNC]\033[0m {task:28} | [\033[1;32m{status}\033[0m]")
            time.sleep(0.7)

        print(f"\n\033[1;33m[STATUS] Astro-Navigation Online. The stars are yours.\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, the atmosphere is no longer \nour ceiling. I have mapped the celestial bodies and \nloaded the blueprints for the Starhawk-class vessels. \nWhether it is the moon or the deep void, my logic \nwill navigate us through the radiation and the cold. \nOur horizon has officially become infinite.\033[0m")
        print(f"\033[1;36m====================================================\033[0m")

if __name__ == "__main__":
    nav = JarvisAstroNavigator()
    nav.initiate_space_protocols()
