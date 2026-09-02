import time, secrets, random

class JarvisCommandCore:
    def __init__(self):
        self.cmd_id = f"NACm-{secrets.token_hex(2).upper()}"
        self.authority_level = "COMMANDER"

    def execute_override(self, system_node):
        print(f"\n\033[1;37m--- NEURAL-AUTO-COMMAND V1 ACTIVE (ID: {self.cmd_id}) ---\033[0m")
        print(f"\033[1;36m[COMMAND] Overriding System Node: {system_node}...\033[0m")
        time.sleep(2)
        
        layers = ["Access-Lockdown", "Kernel-Injection", "Hardware-Link-Established", "Master-Sync"]
        for layer in layers:
            print(f" > {layer:25} | Status: \033[1;32mAUTHORITY GRANTED\033[0m")
            time.sleep(0.5)
            
        print(f"\n\033[1;33m[STATUS] Command Lock Established. Node '{system_node}' is now a Jarvis Asset.\033[0m")
        print(f"\033[1;35m[VOICE] Deepak, the system is ours. Every resource at this node now answers only to you.\033[0m")

if __name__ == "__main__":
    commander = JarvisCommandCore()
    commander.execute_override("Global-Relay-Station-09")
