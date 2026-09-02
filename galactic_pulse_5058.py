import secrets, time, gc

# New Logic: Interative Execution with Visual Triggers
G_DATA = [
    ("\033[1;36m[GALACTIC] P-5054: Warp Drive active. Status: BEYOND-LIGHT.\033[0m"),
    ("\033[1;34m[GALACTIC] P-5055: Interstellar Encryption online. Data: UNBREAKABLE.\033[0m"),
    ("\033[1;32m[GALACTIC] P-5056: Kinetic Energy Harvester online. Power: +25%.\033[0m"),
    ("\033[1;31m[GALACTIC] P-5057: Planetary Magnetic Map ready. Nav: INCH-PERFECT.\033[0m"),
    ("\033[1;35m[GALACTIC] P-5058: Logic v224 synchronized. Space-Time: SECURED.\033[0m")
]

def activate_pulse():
    pulse_id = secrets.token_hex(16).upper()
    print(f"\033[1;37m--- GALACTIC-PULSE CORE INITIALIZED (ID: {pulse_id}) ---\033[0m")
    
    pulse_iterator = iter(G_DATA)
    while True:
        try:
            print(next(pulse_iterator))
            time.sleep(0.1)
        except StopIteration:
            break
            
    print("\033[1;37m" + "="*50 + "\033[0m")
    gc.collect()

if __name__ == "__main__":
    activate_pulse()
