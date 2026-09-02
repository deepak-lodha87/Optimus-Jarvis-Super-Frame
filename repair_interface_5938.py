import time, secrets, gc

class NeuralRepairDrone:
    def __init__(self):
        self.nardi_id = f"NARDI-{secrets.token_hex(4).upper()}"
        self.errors = ["ACTUATOR_JAM", "WIRING_FAULT", "SENSOR_OFFLINE"]
        self.nodes = [
            (5934, "Fault-Detect", "SCANNING FOR PHYSICAL HARDWARE IRREGULARITIES..."),
            (5935, "Actuator-Sync", "SYNCHRONIZING MICRO-REPAIR ARMS..."),
            (5936, "Self-Healing", "INITIATING COMPONENT RE-ROUTING..."),
            (5937, "Life-Predict", "CALCULATING REMAINING SERVICE LIFE..."),
            (5938, "Logic v400", "NARDI-CORE: HARDWARE INTEGRITY VERIFIED.")
        ]

    def perform_repair(self):
        fault = secrets.choice(self.errors)
        print(f"\033[1;31m[!] HARDWARE FAILURE DETECTED: {fault}\033[0m")
        time.sleep(1)
        return f"REPAIR COMPLETE: {fault} HAS BEEN RESOLVED."

    def run_nardi_protocol(self):
        print(f"\033[1;37m--- NEURAL-AUTO-REPAIR-DRONE-INTERFACE ONLINE (ID: {self.nardi_id}) ---\033[0m")
        colors = [36, 35, 34, 32, 31]
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            print(f"\033[1;{colors[i]}m[MODULE:HARDWARE | REPAIR:ACTIVE] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        repair_msg = self.perform_repair()
        print("\033[1;37m" + "="*60 + "\033[0m")
        print(f"\033[1;32m{repair_msg}\033[0m")
        print("\033[1;32mSTATUS: OPTIMUS JARVIS IS MAINTAINING SYSTEM DURABILITY.\033[0m")

if __name__ == "__main__":
    nardi = NeuralRepairDrone()
    nardi.run_nardi_protocol()
