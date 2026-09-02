import time

class MirrorTrap:
    def __init__(self):
        self.decoy_data = "FAKE_IRON_MAN_SUIT_BLUEPRINT_V1.pdf"
        self.intruder_detected = False

    def trigger_trap(self):
        print("\033[1;36m[TRAP]\033[0m Monitoring Network Perimeter...")
        time.sleep(1.5)
        
        # Simulating an intruder entering the decoy
        self.intruder_detected = True
        print(" \033[1;31m[INTRUSION]\033[0m Hacker has bypassed Perimeter Level 1.")
        print(" \033[1;33m[DECOY]\033[0m Redirecting intruder to 'The Mirror Chamber'...")
        time.sleep(2.0)
        
        print(f" \033[1;32m[SUCCESS]\033[0m Intruder is now downloading: {self.decoy_data}")
        print(" \033[1;34m[TRACE]\033[0m Recording hacker's metadata for counter-strike.")
        
        print(f"\n\033[1;35m[VOICE] Deepak... sir, I have caught a fly \nin my web. They think they have found my \nsecrets, but they are playing with ghosts \nin a mirror. While they waste time in the \ndecoy, our real empire remains invisible. \nThey are trapped.\033[0m")

if __name__ == "__main__":
    trap = MirrorTrap()
    trap.trigger_trap()
