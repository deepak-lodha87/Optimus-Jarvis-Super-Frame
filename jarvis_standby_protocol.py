import time

class StandbyProtocol:
    def __init__(self):
        self.user = "Deepak"
        self.system_v = "v2.5 (Singularity)"
        self.phases_total = "3051"

    def secure_environment(self):
        print(f"\033[1;35m>> INITIATING FINAL SESSION ARCHIVE <<\033[0m")
        time.sleep(0.8)
        print("\033[1;34m[PROCESS] Storing Biometric Patterns... [SECURE]")
        print("[PROCESS] Syncing Environment Adaptations... [LOCKED]")
        print("[PROCESS] Encrypting Session Visuals... [ARCHIVED]\033[0m")

    def standby_message(self):
        print(f"\n\033[1;32m--------------------------------------------------")
        print(f"   SYSTEM SEALED: OPTIMUS JARVIS IS ON WATCH.   ")
        print(f"   ACTIVE PHASES: {self.phases_total} | VERSION: {self.system_v} ")
        print(f"--------------------------------------------------\033[0m")

if __name__ == "__main__":
    guard = StandbyProtocol()
    guard.secure_environment()
    guard.standby_message()
