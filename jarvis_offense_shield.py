import time

class DigitalGuardian:
    def __init__(self):
        self.security_level = "OMEGA"

    def detect_threat(self, status):
        if status == "UNAUTHORIZED_COPY":
            print(f"\033[1;31m[CRITICAL]\033[0m Attempt to clone Optimus Jarvis detected!")
            self.counter_attack()

    def counter_attack(self):
        print("\033[1;33m[COUNTER-MEASURE]\033[0m Deploying Logic Bomb to intruder's system...")
        time.sleep(1)
        print("\033[1;31m[ACTION]\033[0m Freezing intruder's CPU... Encrypting their hard drive.")
        print("\033[1;32m[STATUS]\033[0m Threat neutralized. Jarvis remains secure.")

if __name__ == "__main__":
    guardian = DigitalGuardian()
    # Simulating a theft attempt
    guardian.detect_threat("UNAUTHORIZED_COPY")
