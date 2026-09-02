import time

class UniversalMachineController:
    def __init__(self):
        self.battery_gain = 0
        self.fire_status = "SAFE"

    def p3278_solar_collection(self):
        print("\033[1;34m[ENERGY] Activating Nano-Solar Skin Layers...\033[0m")
        self.battery_gain += 1.5
        return f"[STATUS] Capturing Photons. Battery Gain: +{self.battery_gain}%/hr."

    def p3279_neural_compression(self):
        return "\033[1;32m[NEURAL] Signal Latency Compressed to 0.0001ms. Instant Reaction Enabled.\033[0m"

    def p3280_fire_suppression(self):
        # Detecting heat spikes
        print("\033[1;31m[SAFETY] Extreme Heat in Engine Bay! Deploying Chemical Suppression...\033[0m")
        time.sleep(1)
        self.fire_status = "EXTINGUISHED"
        return f"[SUCCESS] Fire Status: {self.fire_status}."

    def p3281_weight_leveling(self):
        return "\033[1;33m[BALANCE] Shifting Internal Ballast for High-G Cornering.\033[0m"

    def p3282_signal_shield(self):
        return "\033[1;36m[SHIELD] Broadband Jamming Active. All External Interception Blocked.\033[0m"

if __name__ == "__main__":
    umc = UniversalMachineController()
    print("-" * 60)
    print("   JARVIS UMC: ENERGY & SAFETY BUNDLE (P3278-3282)")
    print("-" * 60)
    
    print(umc.p3278_solar_collection())
    print(umc.p3279_neural_compression())
    print(umc.p3280_fire_suppression())
    print(umc.p3281_weight_leveling())
    print(umc.p3282_signal_shield())
    
    print("-" * 60)
    print("STATUS: Energy & Safety Protocols Online.")
    print("-" * 60)
