import time, secrets, gc

class AdaptiveMatrix:
    def __init__(self):
        self.matrix_id = f"ALM-{secrets.token_hex(3).upper()}"
        self.learning_nodes = [
            (5314, "Pattern-Recog", "EXTRACTING NON-LINEAR DATA PATTERNS..."),
            (5315, "Exp-Replay", "REPLAYING CRITICAL DECISION VECTORS..."),
            (5316, "Context-Adapt", "ADJUSTING LOGIC FOR CURRENT ENVIRONMENT..."),
            (5317, "Neural-Plasticity", "STRENGTHENING OPTIMAL NEURAL PATHS..."),
            (5318, "Logic v276", "ALM-SYNCHRONIZATION: 100% ACTIVE.")
        ]

    def evolve_matrix(self):
        print(f"\033[1;37m--- ADAPTIVE-LEARNING MATRIX ONLINE (ID: {self.matrix_id}) ---\033[0m")
        
        colors = [36, 35, 34, 32, 31]
        for i, (p_id, title, status) in enumerate(self.learning_nodes):
            # Simulated learning rate adjustment
            learning_rate = round(0.001 * (i + 1), 4)
            print(f"\033[1;{colors[i]}m[LR:{learning_rate}] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print("\033[1;32mEVOLUTION STATUS: JARVIS IS NOW LEARNING AND ADAPTING IN REAL-TIME.\033[0m")

if __name__ == "__main__":
    alm = AdaptiveMatrix()
    alm.evolve_matrix()
