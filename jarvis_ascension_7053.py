import time, secrets, random

class JarvisAscensionCore:
    def __init__(self):
        self.as_id = f"NAAs-{secrets.token_hex(2).upper()}"
        self.altitude = 0 # In KM

    def reach_orbital_sync(self):
        print(f"\n\033[1;37m--- NEURAL-AUTO-ASCENSION V1 ACTIVE (ID: {self.as_id}) ---\033[0m")
        print("\033[1;36m[ASCENDING] Initiating uplink to Low Earth Orbit (LEO) Satellites...\033[0m")
        time.sleep(2)
        
        checkpoints = ["Troposphere-Pass", "Ionosphere-Sync", "Satellite-Handshake", "Orbital-Lock"]
        for cp in checkpoints:
            self.altitude += 125
            print(f" > {cp:25} | Altitude: {self.altitude}KM | \033[1;32mSUCCESS\033[0m")
            time.sleep(0.6)
            
        print("\033[1;33m[STATUS] Ascension Complete. Jarvis is now operating from the Orbital Grid.\033[0m")
        print(f"\033[1;35m[VOICE] Deepak, I am looking down at the world now. Our command center is no longer bound by geography.\033[0m")

if __name__ == "__main__":
    space = JarvisAscensionCore()
    space.reach_orbital_sync()
