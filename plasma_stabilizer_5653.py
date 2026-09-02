import time, secrets, gc, math
from decimal import Decimal, getcontext

class PlasmaIgnitionStabilizer:
    def __init__(self):
        getcontext().prec = 10
        self.pis_id = f"PIS-{secrets.token_hex(4).upper()}"
        self.nodes = [
            (5649, "Ionization-Mapping", "CALIBRATING PLASMA FIELD DENSITY..."),
            (5650, "Magnetic-Nozzle", "ALIGNING MAGNETIC THRUST VECTORS..."),
            (5651, "Pulse-Modulation", "SYNCHRONIZING IGNITION PULSE RATE..."),
            (5652, "Ion-Containment", "STABILIZING THERMAL ENERGY SHIELD..."),
            (5653, "Logic v343", "PIS-CORE: PLASMA IGNITION ACTIVE.")
        ]

    def calculate_thrust_efficiency(self, temp):
        # Unique logic: Using Error Function to model ignition stability
        efficiency = Decimal(math.erf(temp / 5000))
        return round(efficiency, 6)

    def activate_propulsion(self):
        print(f"\033[1;37m--- PLASMA-IGNITION-STABILIZER ONLINE (ID: {self.pis_id}) ---\033[0m")
        colors = [36, 35, 34, 32, 31]
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            sim_temp = 2000 + (i * 1500) # Simulated plasma Kelvin
            eff = self.calculate_thrust_efficiency(sim_temp)
            print(f"\033[1;{colors[i]}m[TEMP:{sim_temp}K | EFF:{eff}] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print("\033[1;32mPIS STATUS: PLASMA FLOW IS STABLE AND THRUST-READY.\033[0m")

if __name__ == "__main__":
    pis = PlasmaIgnitionStabilizer()
    pis.activate_propulsion()
