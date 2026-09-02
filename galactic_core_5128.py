import secrets, time, gc

def core_generator():
    # Unique data stream for Phase 5124-5128
    logic_stream = [
        (5124, "Stellar-Wind Drift active. Propulsion: 0-FUEL."),
        (5125, "Neutrino Link online. Encryption: UNBREAKABLE."),
        (5126, "Heat Vents active. Signature: INVISIBLE."),
        (5127, "Gravity Sync locked. Navigation: CORE-DRIVEN."),
        (5128, "Logic v238 Sync active. Authority: GALACTIC.")
    ]
    for phase in logic_stream:
        yield phase

def execute_galactic_core():
    print(f"\033[1;37m--- GALACTIC-CORE INITIALIZED (U-ID: {secrets.token_urlsafe(8)}) ---\033[0m")
    
    colors = [36, 31, 32, 34, 35]
    gen = core_generator()
    
    for i in range(5):
        p_id, status = next(gen)
        print(f"\033[1;{colors[i]}m[GALACTIC] Phase {p_id}: {status}\033[0m")
        time.sleep(0.18)

    print("\033[1;37m" + "="*60 + "\033[0m")
    gc.collect()

if __name__ == "__main__":
    execute_galactic_core()
