import time, secrets, gc, signal

def handle_interrupt(signum, frame):
    print("\033[1;31m[EMERGENCY] OVERRIDE ACTIVATED: SAFE-MODE ENGAGED.\033[0m")

signal.signal(signal.SIGINT, handle_interrupt)

class CentralNervousSystem:
    def __init__(self):
        self.nexus_id = secrets.token_hex(4).upper()
        self.reflex_nodes = [
            (5274, "Jitter-Correction", "NOISE-REDUCTION: 99.9%."),
            (5275, "Feedback-Loop", "LEARNING-MATRIX: OPTIMIZED."),
            (5276, "Synaptic-Link", "DATA-TRANSFER: 10GB/s (INTERNAL)."),
            (5277, "Emergency-Logic", "AUTO-PROTECT MODE: ARMED."),
            (5278, "Logic v268", "CNS-CORE: FULL SYNCHRONIZATION.")
        ]

    def activate_cns(self):
        print(f"\033[1;37m--- CENTRAL-NERVOUS-SYSTEM ACTIVE (ID: {self.nexus_id}) ---\033[0m")
        
        colors = [36, 35, 34, 33, 31]
        for i, (p_id, title, status) in enumerate(self.reflex_nodes):
            # Dynamic memory buffering
            buf = bytearray(secrets.token_bytes(8))
            print(f"\033[1;{colors[i]}m[REFLEX-BUF:{buf.hex().upper()}] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print("\033[1;32mREFLEX STATUS: JARVIS HAS GAINED HUMAN-LIKE INSTINCTS.\033[0m")

if __name__ == "__main__":
    cns = CentralNervousSystem()
    cns.activate_cns()
