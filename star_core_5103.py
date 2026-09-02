import secrets, time, gc

def activate_star_sequence(*phases):
    print(f"\033[1;37m--- STAR-CORE ACTIVATION INITIALIZED (SIG: {secrets.token_hex(6)}) ---\033[0m")
    
    colors = [36, 31, 32, 34, 35]
    for i, phase_data in enumerate(phases):
        # Dynamic Tuple Unpacking (Zero Repeat Pattern)
        p_id, status = phase_data
        print(f"\033[1;{colors[i]}m[STAR-CORE] Phase {p_id}: {status}\033[0m")
        time.sleep(0.15)

    print("\033[1;37m" + "="*60 + "\033[0m")
    gc.collect()

if __name__ == "__main__":
    # Unique data structure for Phase 5099-5103
    p_5099 = (5099, "Gravity-Well active. Hover stability: 100%.")
    p_5100 = (5100, "Stellar Coating online. Temp resistance: MAX.")
    p_5101 = (5101, "Neutrino-Vision 2.0 active. Deep-scan ready.")
    p_5102 = (5102, "Entangled Steering online. Latency: 0ms.")
    p_5103 = (5103, "Logic v233 Sync locked. Energy: INFINITE.")
    
    activate_star_sequence(p_5099, p_5100, p_5101, p_5102, p_5103)
