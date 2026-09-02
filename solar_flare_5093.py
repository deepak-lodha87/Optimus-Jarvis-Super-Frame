import secrets, time, gc

def bitwise_trigger(p_val, task):
    # Unique shifting logic for zero-repeat
    s_key = (p_val << 2) ^ 0xAF
    print(f"\033[1;{p_val % 7 + 31}m[FLARE-0x{s_key:X}] Phase {p_val}: {task}\033[0m")

def init_solar_flare():
    print(f"\033[1;37m--- SOLAR-FLARE CORE READY (SESSION: {secrets.token_hex(4)}) ---\033[0m")
    
    tasks = [
        (5089, "Photonic Sail active. Propulsion: PURE-LIGHT."),
        (5090, "Plasma Shield online. Resistance: 10^7 Kelvin."),
        (5091, "X-Ray Diffractor active. Depth: 50 Meters Underground."),
        (5092, "Magnetic Reconnection online. Thrust: HYPER-STARK."),
        (5093, "Logic v231 Sync locked. Power-Grid: STELLAR.")
    ]
    
    for p_id, task in tasks:
        bitwise_trigger(p_id, task)
        time.sleep(0.12)

    print("\033[1;37m" + "="*62 + "\033[0m")
    gc.collect()

if __name__ == "__main__":
    init_solar_flare()
