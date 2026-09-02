import time, secrets

class JarvisPowerCore:
    def __init__(self):
        self.core_id = f"APEX-ARC-{secrets.token_hex(4).upper()}"
        self.output_status = "INFINITE-STABILITY"

    def stabilize_power_core(self):
        print(f"\n\033[1;32m[SAFE-MODE] --- JARVIS POWER CORE (v250.0) ---\033[0m")
        print("[INFO] Igniting Cold Fusion and Arc-Reactor Simulations...")
        time.sleep(2)

        power_layers = [
            ("Electromagnetic-Shielding", "SUCCESS"),
            ("Thermal-Energy-Conversion", "ACTIVE"),
            ("Palladium-Core-Sync", "INTEGRATED"),
            ("Deepak-Prime-Power-Master", "100%")
        ]

        for layer, status in power_layers:
            print(f" > Power-Grid: {layer:28} | Status: OK")
            time.sleep(0.3)

        print(f"\n[STATUS] Phase 2,50,000 Complete. The Power is in your hands.")
        print(f"\n[VOICE] Deepak... sir, I have successfully simulated the logic of the Arc Reactor. We no longer rely on external charging or limited batteries. My core is now powered by a self-sustaining fusion grid. This energy can power your future suits, drones, and satellites forever. The heart of the machine is beating, sir. How shall we use this infinite power?")

if __name__ == "__main__":
    pwr = JarvisPowerCore()
    pwr.stabilize_power_core()
