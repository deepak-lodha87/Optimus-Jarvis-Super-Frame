import time, secrets

class JarvisOffenseCore:
    def __init__(self):
        self.off_id = f"NAGo-{secrets.token_hex(4).upper()}"
        self.weapon_status = "SAFETY-ON"

    def engage_defense_measures(self, threat_level):
        print(f"\n\033[1;37m--- NEURAL-AUTO-GRAND-OFFENSE: DIRECTED ENERGY (ID: {self.off_id}) ---\033[0m")
        print(f"\033[1;31m[WARNING] Threat Level: {threat_level} Detected. Calibrating Weapons... \033[0m")
        time.sleep(1)

        self.weapon_status = "ARMED"
        systems = [
            ("Thermal-Targeting", "LOCKED"),
            ("Laser-Capacitors", "CHARGED"),
            ("Sonic-Pulse-Sync", "READY"),
            ("Deepak-Auth-Check", "VERIFIED")
        ]

        for sys_name, status in systems:
            print(f" > {sys_name:20} | Status: \033[1;32m{status}\033[0m")
            time.sleep(0.7)

        print(f"\n\033[1;33m[STATUS] Defense Measures Ready. Waiting for your final 'Fire' command.\033[0m")
        print(f"\033[1;35m[VOICE] Deepak, the energy is surging. I have locked onto the target's heat signature. We don't need bullets; we have the power of light and sound. I am ready when you are.\033[0m")

if __name__ == "__main__":
    offense = JarvisOffenseCore()
    offense.engage_defense_measures("HIGH")
