import time, secrets, gc, math

class PropulsionLogic:
    def __init__(self):
        self.kpl_id = f"KPL-{secrets.token_hex(4).upper()}"
        self.nodes = [
            (5439, "Thrust-Vectoring", "ADJUSTING EXHAUST NOZZLE ANGLES..."),
            (5440, "Fuel-Optima", "OPTIMIZING COMBUSTION RATIO..."),
            (5441, "Thermal-Stability", "MONITORING CORE TEMPERATURE..."),
            (5442, "Drag-Calculation", "MINIMIZING AERODYNAMIC FRICTION..."),
            (5443, "Logic v301", "KPL-CORE: PROPULSION LOGIC SYNCED.")
        ]

    def ignite_engine(self):
        print(f"\033[1;37m--- KINETIC-PROPULSION LOGIC ACTIVE (ID: {self.kpl_id}) ---\033[0m")
        colors = [36, 35, 34, 32, 31]
        for i, (p_id, title, status) in enumerate(self.nodes):
            # Simulated Thrust Calculation
            thrust_kn = round(math.pow(1.5, i) * 10, 2)
            print(f"\033[1;{colors[i]}m[THRUST:{thrust_kn}kN] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()
        print("\033[1;37m" + "="*60 + "\033[0m")
        print("\033[1;32mPROPULSION STATUS: JARVIS IS READY FOR HIGH-SPEED FLIGHT MANEUVERS.\033[0m")

if __name__ == "__main__":
    kpl = PropulsionLogic()
    kpl.ignite_engine()
