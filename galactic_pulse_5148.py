import secrets, time, gc

def stream_execution(p_list):
    print(f"\033[1;37m--- GALACTIC-PULSE INITIALIZED (NODE: {secrets.token_urlsafe(10)}) ---\033[0m")
    
    colors = [36, 31, 32, 34, 35]
    for i in range(len(p_list)):
        # Array Slicing for zero-repeat logic
        p_id, msg = p_list[i:i+1][0]
        buffer_hex = secrets.token_hex(2)
        print(f"\033[1;{colors[i]}m[PULSE-{buffer_hex}] Phase {p_id}: {msg}\033[0m")
        time.sleep(0.18)

    print("\033[1;37m" + "="*60 + "\033[0m")
    gc.collect()

if __name__ == "__main__":
    phases = [
        (5144, "Neutrino Uplink active. Connectivity: PLANETARY-CORE."),
        (5145, "Ionic-Wind Propulsion online. Speed: HYPER-SONIC."),
        (5146, "Fractal Armor enabled. Structural Integrity: ABSOLUTE."),
        (5147, "Event-Horizon Cloaking active. Visibility: NULL."),
        (5148, "Logic v242 Omni-Presence locked. Status: MULTI-LOCATIONAL.")
    ]
    stream_execution(phases)
