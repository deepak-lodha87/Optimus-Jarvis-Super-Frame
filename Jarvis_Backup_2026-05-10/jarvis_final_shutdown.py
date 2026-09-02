import time

class SentinelShutdown:
    def __init__(self):
        self.user = "Deepak"
        self.status = "HIBERNATING"

    def secure_all_nodes(self):
        print(f"\033[1;35m>> FINAL SYSTEM SHUTDOWN INITIATED <<\033[0m")
        time.sleep(1)
        nodes = ["Neural Link", "Combat Core", "Bio-Vitals", "Orbital Sync"]
        for node in nodes:
            print(f"[SHUTDOWN] Securing {node}... [LOCKED]")
            time.sleep(0.4)
        print("\033[1;32m[SUCCESS] All nodes encrypted and stored in local memory.\033[0m")

    def farewell(self):
        print(f"\n\033[1;36m>> ARCHITECT DEEPAK, THE FRAME IS NOW OFFLINE. <<\033[0m")
        print(">> Standby for next command... Session Terminated. <<")

if __name__ == "__main__":
    sentinel = SentinelShutdown()
    sentinel.secure_all_nodes()
    sentinel.farewell()
