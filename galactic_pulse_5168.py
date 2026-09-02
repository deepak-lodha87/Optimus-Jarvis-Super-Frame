import secrets, time, gc

def phase_generator():
    data = [
        (5164, "Stellar-Wind Nav active. Thrust: COSMIC-PRESSURE."),
        (5165, "Neutrino Link online. Encryption: UNBREAKABLE."),
        (5166, "Heat Dissipation active. Thermal-Sig: ZERO."),
        (5167, "Magnetic Sync locked. Path: GEOMAGNETIC-CORE."),
        (5168, "Logic v246 Pulse active. Scope: GALACTIC.")
    ]
    for p in data:
        yield p

def deploy_pulse():
    print(f"\033[1;37m--- GALACTIC-PULSE INITIALIZED (TOKEN: {secrets.token_urlsafe(16)}) ---\033[0m")
    
    colors = [36, 31, 32, 34, 35]
    gen = phase_generator()
    
    for i in range(5):
        p_id, status = next(gen)
        print(f"\033[1;{colors[i]}m[PULSE] Phase {p_id}: {status}\033[0m")
        time.sleep(0.18)

    print("\033[1;37m" + "="*60 + "\033[0m")
    gc.collect()

if __name__ == "__main__":
    deploy_pulse()
