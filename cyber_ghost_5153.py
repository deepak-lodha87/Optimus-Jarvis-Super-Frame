import secrets, time, gc

class GhostModule:
    def __init__(self, p_id, task):
        self.p_id = p_id
        self.task = task
        self.token = secrets.token_hex(3).upper()

    def deploy(self, hex_color):
        print(f"\033[1;{hex_color}m[GHOST-{self.token}] Phase {self.p_id}: {self.task}\033[0m")

def init_ghost_protocol():
    print(f"\033[1;37m--- CYBER-GHOST CORE INITIALIZED (ID: {secrets.token_urlsafe(12)}) ---\033[0m")
    
    modules = [
        GhostModule(5149, "Deep-Packet Masking active. Status: UNTRACEABLE."),
        GhostModule(5150, "Bio-Synthetic Sensor Link online. Input: MULTI-BIOMETRIC."),
        GhostModule(5151, "EMP Dampening active. System: HARDENED."),
        GhostModule(5152, "Shadow-Node Relay enabled. Path: DECENTRALIZED."),
        GhostModule(5153, "Logic v243 Infiltration locked. Security: OVERRIDDEN.")
    ]
    
    colors = [36, 31, 32, 34, 35]
    for i, mod in enumerate(modules):
        mod.deploy(colors[i])
        time.sleep(0.2)

    print("\033[1;37m" + "="*60 + "\033[0m")
    gc.collect()

if __name__ == "__main__":
    init_ghost_protocol()
