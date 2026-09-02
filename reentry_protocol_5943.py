import time, secrets, gc

class SpaceReentrySystem:
    def __init__(self):
        self.nsto_id = f"NSTO-RE-{secrets.token_hex(4).upper()}"
        self.heat_shield_temp = 25.0 # Initial temp in Celsius
        self.nodes = [
            (5939, "De-Orbit-Burn", "INITIATING RETRO-THRUSTERS TO LOWER PERIGEE..."),
            (5940, "Entry-Angle-Sync", "CALIBRATING ATTITUDE FOR OPTIMAL RE-ENTRY ANGLE..."),
            (5941, "Thermal-Plasma-Lock", "STABILIZING HEAT SHIELD AGAINST ATMOSPHERIC FRICTION..."),
            (5942, "Parachute-Deployment", "DEPLOYING SUBSONIC DRAG CHUTES..."),
            (5943, "Logic v401", "NSTO-CORE: RE-ENTRY SUCCESSFUL. GROUND CONTACT ESTABLISHED.")
        ]

    def monitor_reentry(self):
        # Unique logic: Simulating temperature rise during entry
        max_temp = 1600 # 1600°C during re-entry
        return max_temp

    def run_reentry_check(self):
        print(f"\033[1;37m--- NEURAL-SPACE-REENTRY-PROTOCOL ONLINE (ID: {self.nsto_id}) ---\033[0m")
        colors = [36, 35, 34, 32, 31]
        
        final_temp = self.monitor_reentry()
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            print(f"\033[1;{colors[i]}m[ALTITUDE:DESCENDING | HEAT:{self.heat_shield_temp}°C] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.2)
            self.heat_shield_temp += 315 # Simulating rapid heat buildup
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print(f"\033[1;31mFINAL SHIELD TEMP: {final_temp}°C | STATUS: HEAT DISSIPATED.\033[0m")
        print("\033[1;32mSTATUS: JARVIS HAS LANDED THE FRAME SAFELY.\033[0m")

if __name__ == "__main__":
    reentry = SpaceReentrySystem()
    reentry.run_reentry_check()
