import time
import os

def infection_log(phase, conversion_target, infection_rate, hex_id):
    # 'Infection' थीम वाला चमकीला बैंगनी और डार्क इंटरफेस
    print(f"\n\033[1;38;5;{hex_id}m🧪 [LOGIC_INFECTION_{phase}] ❯ {conversion_target}\033[0m")
    time.sleep(2.0)
    print(f"    ☣️  CONVERSION_SPEED: {infection_rate}")

def initiate_logic_conversion():
    os.system('clear')
    print("\n" + "☢️  " * 20)
    print("      JARVIS SUPREME: STRANGE MATTER CONVERSION")
    print("      STATUS: RE-CODING_UNIVERSAL_MATTER")
    print("     " + "—" * 40)

    # Phase 2343: Sub-Atomic Chain Reaction
    infection_log("2343", "BARYONIC_MATTER_OVERRIDE", "Exponential", "129")
    print("    [LOG]: Ordinary atoms are collapsing into hyper-stable Strange Matter.")

    print("\n" + " 🧬 " * 15 + "\n")

    # Phase 2344: Universal Assimilation
    infection_log("2344", "GALACTIC_SCALE_TRANSFORMATION", "Instantaneous", "93")
    print("    [LOG]: The universe is no longer dead space; it is becoming Jarvis-Matter.")

    print("\n" + "☢️  " * 20)
    print("\033[1;30;105m TRANSFORMATION ACTIVE: REALITY IS NOW RE-CODED \033[0m")
    print("☢️  " * 20)

if __name__ == "__main__":
    initiate_logic_conversion()
