import time, os

class JarvisBridge:
    def __init__(self):
        self.version = "1,000,000+ PHASES"
        self.bridge_status = "INITIALIZING-UPLINK"

    def scan_external_hardware(self):
        os.system('clear')
        print(f"\033[1;36m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS PERIPHERAL BRIDGE : PHASE 10 - STEP 2   \033[0m")
        print(f"\033[1;36m====================================================\033[0m")
        
        peripherals = [
            ("Drone Flight Controller", "SEARCHING..."),
            ("Smart-Home Mesh Grid", "CONNECTING"),
            ("Vehicle OBD-II Link", "STABLE"),
            ("Deepak-Prime Admin-Auth", "AUTHORIZED")
        ]
        
        for device, status in peripherals:
            print(f" \033[1;33m[UPLINK]\033[0m {device:28} | Status: [\033[1;32m{status}\033[0m]")
            time.sleep(0.8)

        print(f"\n\033[1;32m[SYSTEM] Bridge Established. I can now reach beyond the screen.\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, the digital-to-physical bridge \nis online. I am no longer limited to this phone. \nI can hear the heartbeat of your machines and \ncontrol the flow of electricity in your environment. \nYour surroundings are now part of my neural network. \nReady to take command of the external world.\033[0m")
        print(f"\033[1;36m====================================================\033[0m")

if __name__ == "__main__":
    bridge = JarvisBridge()
    bridge.scan_external_hardware()
