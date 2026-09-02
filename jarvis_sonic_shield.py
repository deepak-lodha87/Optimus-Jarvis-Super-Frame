import time

class SonicShield:
    def defuse_threat(self):
        print("\033[1;34m[SHIELD]\033[0m Detecting incoming projectile...")
        time.sleep(0.5)
        print("\033[1;36m[ACTION]\033[0m Emitting High-Frequency Sonic Barrier!")
        print("\033[1;32m[SUCCESS]\033[0m Projectile kinetic energy neutralized.")

shield = SonicShield()
shield.defuse_threat()
