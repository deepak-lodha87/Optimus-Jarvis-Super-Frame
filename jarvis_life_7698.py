import time, secrets

class JarvisLifeSupport:
    def __init__(self):
        self.ls_id = f"NAGat-{secrets.token_hex(4).upper()}"
        self.internal_temp = 25 # Celsius
        self.oxygen_level = 100 # Percentage

    def activate_survival_protocol(self):
        print(f"\n\033[1;37m--- NEURAL-AUTO-GRAND-ATMOSPHERE: LIFE SUPPORT (ID: {self.ls_id}) ---\033[0m")
        print("\033[1;36m[ENV] Initiating Internal Atmosphere Stabilization... \033[0m")
        time.sleep(1)

        vitals = [
            ("Cabin-Pressure", "1.0 ATM"),
            ("Thermal-Grid", "25°C"),
            ("Oxygen-Scrubbers", "ACTIVE"),
            ("Radiation-Hull", "LOCKED")
        ]

        for system, status in vitals:
            print(f" > {system:20} | Status: \033[1;32m{status}\033[0m")
            time.sleep(0.7)

        print(f"\n\033[1;33m[STATUS] Life Support Online. Environment is now safe for Deepak.Protocol.\033[0m")
        print(f"\033[1;35m[VOICE] Deepak, the air is thin up here, but inside our frame, it is as fresh as a morning in Ratlam. I am monitoring your vitals. You are safe to explore the edge of space.\033[0m")

if __name__ == "__main__":
    support = JarvisLifeSupport()
    support.activate_survival_protocol()
