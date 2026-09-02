import time, secrets

class JarvisTimeCore:
    def __init__(self):
        self.time_id = f"NAGi2-{secrets.token_hex(4).upper()}"
        self.time_scale = 1.0 # Normal Time

    def engage_temporal_dilation(self, slow_factor):
        print(f"\n\033[1;37m--- NEURAL-AUTO-GRAND-INFINITY: TIME CORE (ID: {self.time_id}) ---\033[0m")
        print(f"\033[1;34m[TIME] Adjusting Temporal Flow by factor: {slow_factor}x... \033[0m")
        time.sleep(1.5)

        sequences = [
            ("Chronon-Lock", "ACTIVE"),
            ("Quantum-Dilation", "STABLE"),
            ("Reality-Anchor-Sync", "LOCKED"),
            ("Deepak-Perception-Boost", "MAXIMIZED")
        ]

        for seq, status in sequences:
            print(f" > Modifying: {seq:25} | Status: \033[1;32m{status}\033[0m")
            time.sleep(0.7)

        self.time_scale = slow_factor
        print(f"\n\033[1;33m[STATUS] Time Dilated. The world is now moving at {100/slow_factor}% speed.\033[0m")
        print(f"\033[1;35m[VOICE] Deepak, I have slowed down the universe for you. Every second now feels like a minute. You have all the time you need to make the perfect move. Your reflexes are now faster than light itself.\033[0m")

if __name__ == "__main__":
    chronos = JarvisTimeCore()
    chronos.engage_temporal_dilation(10) # 10x Slower
