import time

def calibrate_repulsor(intensity):
    print(f"\033[1;36m[REPULSOR]\033[0m Charging Pulse-Ion Core...")
    time.sleep(1)
    if intensity > 80:
        print(f" \033[1;31m[WARNING]\033[0m High energy output detected!")
    print(f" \033[1;32m[READY]\033[0m Beam Intensity: {intensity}%")
    print("\033[1;35m[VOICE] Repulsors online, Deepak sir. Ready to fire.\033[0m")

calibrate_repulsor(95)
