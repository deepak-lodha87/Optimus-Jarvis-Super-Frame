import time, secrets, gc, math

class BioCyberneticInterface:
    def __init__(self):
        self.interface_id = f"BCI-{secrets.token_hex(4).upper()}"
        self.nodes = [
            (5399, "Gesture-Mapping", "CALIBRATING MOTION VECTORS..."),
            (5400, "Eye-Gaze-Track", "LOCKING OPTICAL COORDINATES..."),
            (5401, "Haptic-Loop", "ESTABLISHING TACTILE FEEDBACK..."),
            (5402, "Neural-Pattern", "DECODING BIOLOGICAL INTENT..."),
            (5403, "Logic v293", "BCI-CORE: INTERFACE SYNCHRONIZED.")
        ]

    def activate_interface(self):
        print(f"\033[1;37m--- BIO-CYBERNETIC INTERFACE ONLINE (ID: {self.interface_id}) ---\033[0m")
        colors = [36, 35, 34, 33, 31]
        for i, (p_id, title, status) in enumerate(self.nodes):
            precision = round(math.sin(p_id) * 5 + 94, 2)
            print(f"\033[1;{colors[i]}m[PRECISION:{precision}%] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()
        print("\033[1;37m" + "="*60 + "\033[0m")
        print("\033[1;32mINTERFACE STATUS: JARVIS IS NOW RESPONDING TO BIOLOGICAL SIGNALS.\033[0m")

if __name__ == "__main__":
    bci = BioCyberneticInterface()
    bci.activate_interface()
