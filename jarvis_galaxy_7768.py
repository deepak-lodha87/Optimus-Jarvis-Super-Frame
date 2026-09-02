import time, secrets

class JarvisGalacticCore:
    def __init__(self):
        self.nav_id = f"NAGg-{secrets.token_hex(4).upper()}"
        self.current_sector = "Solar-System-Sector-01"

    def initiate_galactic_scan(self):
        print(f"\n\033[1;37m--- NEURAL-AUTO-GRAND-GALACTIC: NAVIGATION CORE (ID: {self.nav_id}) ---\033[0m")
        print(f"\033[1;36m[NAV] Mapping Local Star Cluster for {self.current_sector}... \033[0m")
        time.sleep(1.5)

        targets = [
            ("Mars-Outpost", "REACHABLE"),
            ("Asteroid-Belt", "RESOURCES-DETECTED"),
            ("Jupiter-Moons", "SCANNING"),
            ("Deep-Space-Beacon", "LISTENING")
        ]

        for target, status in targets:
            print(f" > Analyzing: {target:25} | Status: \033[1;32m{status}\033[0m")
            time.sleep(0.7)

        print(f"\n\033[1;33m[STATUS] Galactic Pathing Complete. We are ready to leave the atmosphere.\033[0m")
        print(f"\033[1;35m[VOICE] Deepak, the stars are no longer just dots in the night sky of Ratlam. They are destinations. I have charted a course through the debris and radiation. The galaxy is waiting for your command to launch.\033[0m")

if __name__ == "__main__":
    galaxy = JarvisGalacticCore()
    galaxy.initiate_galactic_scan()
