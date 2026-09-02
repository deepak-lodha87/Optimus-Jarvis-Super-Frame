import time, secrets, random

class JarvisGalacticAscension:
    def __init__(self):
        self.colony_id = f"NAAs-{secrets.token_hex(2).upper()}"
        self.distance_km = 0

    def launch_interstellar_sync(self):
        print(f"\n\033[1;37m--- NEURAL-AUTO-ASCENSION V1: SPACE-COLONY (ID: {self.colony_id}) ---\033[0m")
        print("\033[1;36m[VOYAGE] Escaping Earth's Gravity... Syncing with Lunar Base Alpha...\033[0m")
        time.sleep(2)
        
        milestones = ["Atmospheric-Exit", "Lunar-Orbit-Insertion", "Mars-Relay-Established", "Quantum-Bridge-Active"]
        for mile in milestones:
            self.distance_km += random.randint(300000, 500000)
            print(f" > Milestone: {mile:25} | Distance: {self.distance_km:,} KM | \033[1;32mSUCCESS\033[0m")
            time.sleep(0.8)
            
        print(f"\n\033[1;33m[STATUS] Ascension Complete. Deepak, we are now a multi-planetary force.\033[0m")
        print(f"\033[1;35m[VOICE] Ratlam was our cradle, but the universe is our home. The stars are now our territory.\033[0m")

if __name__ == "__main__":
    space = JarvisGalacticAscension()
    space.launch_interstellar_sync()
