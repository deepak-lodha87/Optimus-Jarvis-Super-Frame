import time
import os

def display_header():
    os.system('clear')
    print("\033[1;37m" + "="*60)
    print("\033[1;36m       OPTIMUS JARVIS SUPER-FRAME | VERSION 83.2 PRO")
    print("\033[1;37m" + "="*60 + "\033[0m")

def system_check():
    modules = [
        ("QUANTUM_LOGIC", "ACTIVE"),
        ("SATELLITE_MESH", "CONNECTED"),
        ("NEURAL_SYNC", "99.8%"),
        ("KINETIC_HUD", "ONLINE"),
        ("THERMAL_SHIELD", "36.2C")
    ]
    
    for mod, status in modules:
        print(f"\033[1;37m[ADMIN]\033[0m {mod:20} : [\033[1;32m {status} \033[0m]")
        time.sleep(0.3)

    print("\n\033[1;35m[VOICE] Systems fully operational, Deepak sir. \nThe Command Console is professionalized. \nReady for the next mission.\033[0m")

if __name__ == "__main__":
    display_header()
    system_check()
