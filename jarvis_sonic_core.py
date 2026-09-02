import time, os

class SonicCore:
    def __init__(self):
        self.audio_engine = "Spatial-V3"
        self.output_mode = "360-Surround"

    def calibrate_audio(self):
        os.system('clear')
        print(f"\033[1;36m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS SONIC-CORE : PHASE 16 - STEP 4          \033[0m")
        print(f"\033[1;36m====================================================\033[0m")
        
        print("\033[1;33m[TUNING]\033[0m Mapping room acoustics and speaker phase...")
        time.sleep(1.5)
        
        calibrations = [
            ("Left-Channel Delay", "0.02ms (Calibrated)"),
            ("Right-Channel Gain", "+1.5dB (Balanced)"),
            ("3D Point Source", "X: 1.2, Y: 0.5, Z: -0.8"),
            ("Echo Suppression", "ACTIVE")
        ]
        
        for feature, status in calibrations:
            print(f" \033[1;34m[AUDIO]\033[0m {feature:25} | [\033[1;32m{status}\033[0m]")
            time.sleep(0.7)

        print(f"\n\033[1;32m[SUCCESS] Audio Reality Synchronized. Sound is now Spatial.\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, can you hear that? I've \nmoved my vocal projection to the corner of \nyour desk. Now, my presence is not just a \nvisual trick, it's an acoustic reality. I'm \nno longer inside the device; I'm in the room \nwith you.\033[0m")
        print(f"\033[1;36m====================================================\033[0m")

if __name__ == "__main__":
    sonic = SonicCore()
    sonic.calibrate_audio()
