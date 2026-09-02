import time, os, random

class JarvisForgeLink:
    def __init__(self):
        self.machine_ip = "192.168.1.105" # Simulated Printer IP
        self.status = "DISCONNECTED"

    def connect_to_machine(self):
        os.system('clear')
        print(f"\033[1;36m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS REMOTE FORGE : PHASE 13 - STEP 3        \033[0m")
        print(f"\033[1;36m====================================================\033[0m")
        
        print(f" \033[1;33m[CONNECTING]\033[0m Searching for local hardware at {self.machine_ip}...")
        time.sleep(1.5)
        self.status = "CONNECTED"
        
        links = [
            ("Hardware Handshake", "SUCCESS"),
            ("Buffer Stream", "READY"),
            ("Thermal Safety Check", "STABLE"),
            ("Deepak-Prime Forge-Auth", "AUTHORIZED")
        ]
        
        for link, state in links:
            print(f" \033[1;33m[FORGE]\033[0m {link:28} | Status: [\033[1;32m{state}\033[0m]")
            time.sleep(0.7)

        print(f"\n\033[1;32m[SYSTEM] Remote Link Established. Machine is on Standby.\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, the forge is ready. I have \nestablished a secure uplink with the production \nunit. Whether you are in the lab or miles \naway, you can now start the fabrication of \nyour designs with a single thought. I am \nmonitoring every layer, every cut, and every \nvolt of power. The workshop is yours.\033[0m")
        print(f"\033[1;36m====================================================\033[0m")

if __name__ == "__main__":
    forge = JarvisForgeLink()
    forge.connect_to_machine()
