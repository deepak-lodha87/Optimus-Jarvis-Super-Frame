import time, secrets

class JarvisGravityDrive:
    def __init__(self):
        self.drive_id = f"NAGg-{secrets.token_hex(4).upper()}"
        self.field_strength = 0

    def engage_anti_gravity(self):
        print(f"\n\033[1;37m--- NEURAL-AUTO-GRAND-GRAVITY: ANTI-GRAVITY DRIVE (ID: {self.drive_id}) ---\033[0m")
        print("\033[1;34m[DRIVE] Modifying Local Gravitational Constant... \033[0m")
        time.sleep(1)

        stages = ["Field-Polarization", "Inertial-Dampening", "Zero-G-Alignment", "Levitation-Lock"]
        for stage in stages:
            self.field_strength += 25
            print(f" > {stage:22} | Power: {self.field_strength}% | Status: \033[1;32mSTABLE\033[0m")
            time.sleep(0.7)

        print(f"\n\033[1;33m[STATUS] Levitation Achieved. The frame is now weightless.\033[0m")
        print(f"\033[1;35m[VOICE] Deepak, we have broken the chains of Earth. The weight of the world no longer applies to us. I have achieved a perfect hover. We are ready to soar beyond the clouds.\033[0m")

if __name__ == "__main__":
    drive = JarvisGravityDrive()
    drive.engage_anti_gravity()
