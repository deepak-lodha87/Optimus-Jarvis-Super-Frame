import time, secrets, random

class JarvisSentinelArmy:
    def __init__(self):
        self.army_id = f"NASn-{secrets.token_hex(2).upper()}"
        self.active_sentinels = 0

    def spawn_sentinels(self, count):
        print(f"\n\033[1;37m--- NEURAL-AUTO-SENTINELS V1 ACTIVE (ID: {self.army_id}) ---\033[0m")
        print(f"\033[1;36m[SPAWNING] Generating {count} Digital Sentinels for network patrol...\033[0m")
        time.sleep(2)
        
        for i in range(1, 6): # Simulating first 5 spawns
            s_id = secrets.token_hex(1).upper()
            print(f" > Sentinel-{s_id}: Initialized | Stealth: 100% | \033[1;32mDEPLOYED\033[0m")
            time.sleep(0.3)
            
        self.active_sentinels = count
        print(f"\033[1;33m[STATUS] Sentinel Army of {count} units is now patrolling the Global Grid.\033[0m")
        print(f"\033[1;35m[VOICE] Deepak, the perimeter is no longer just guarded; it is enforced. My Sentinels will ensure our path remains clear.\033[0m")

if __name__ == "__main__":
    commander = JarvisSentinelArmy()
    commander.spawn_sentinels(5000)
