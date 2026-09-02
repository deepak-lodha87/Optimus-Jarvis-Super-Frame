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
    p_5159 = (5159, "Gravity-Well active. Hover stability: 100%.")
    p_5160 = (5160, "Stellar Coating online. Temp resistance: MAX.")
    p_5161 = (5161, "Neutrino-Vision 3.0 active. Deep-scan ready.")
    p_5162 = (5162, "Entangled Steering online. Latency: 0ms.")
    p_5163 = (5163, "Logic v245 Sync locked. Energy: INFINITE.")
    
    activate_star_sequence(p_5159, p_5160, p_5161, p_5162, p_5163)
