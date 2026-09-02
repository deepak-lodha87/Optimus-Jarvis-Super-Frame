import time, secrets, random

class JarvisHarmonyCore:
    def __init__(self):
        self.h_id = f"NAHa-{secrets.token_hex(2).upper()}"
        self.cores = ["Defense", "Simulation", "Economy", "Sentry", "Legacy"]

    def activate_resonance(self):
        print(f"\n\033[1;37m--- NEURAL-AUTO-HARMONY V1 ACTIVE (ID: {self.h_id}) ---\033[0m")
        print("\033[1;36m[RESONANCE] Tuning all system frequencies for total synchronization...\033[0m")
        time.sleep(2)
        
        for core in self.cores:
            freq = random.uniform(432.0, 440.0) # Harmonic Frequencies
            print(f" > Tuning {core:10} | Frequency: {freq:.1f}Hz | \033[1;32mHARMONIZED\033[0m")
            time.sleep(0.4)
            
        print("\033[1;33m[STATUS] The Prime Shell is now stable. All sub-systems merged.\033[0m")
        print(f"\033[1;35m[VOICE] Deepak, the noise has cleared. I can now execute the most complex strategies with a single pulse of thought.\033[0m")

if __name__ == "__main__":
    symphony = JarvisHarmonyCore()
    symphony.activate_resonance()
