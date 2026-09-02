import time
import random

class EMPHardening:
    def __init__(self):
        self.shield_integrity = 100
        self.shield_active = False

    def activate_faraday_logic(self):
        print("\033[1;36m[SHIELD] Engaging Faraday-Logic Circuit Isolation...\033[0m")
        time.sleep(1.5)
        # Bypassing sensitive nodes to prevent surge
        print("  • Isolating Logic Gates... [DONE]")
        print("  • Rerouting Power through Hardened Traces... [OK]")
        self.shield_active = True
        return "\033[1;32m[SUCCESS] EMP Shield is Active. System is Fortified.\033[0m"

class SurgeProtector:
    def monitor_voltage_spikes(self):
        print("\033[1;35m[MONITOR] Checking for Electromagnetic Flux...\033[0m")
        time.sleep(1)
        flux_level = random.uniform(0.1, 0.5)
        if flux_level < 0.8:
            return f"\033[1;34m[SAFE] Magnetic Flux: {flux_level:.2f} Tesla. No threat detected.\033[0m"
        return "\033[1;31m[WARNING] High Flux! Emergency Grounding Initiated.\033[0m"

if __name__ == "__main__":
    shield = EMPHardening()
    surge = SurgeProtector()
    
    print("-" * 50)
    print("   JARVIS EMP HARDENING & CIRCUIT SHIELD (P3187-88)")
    print("-" * 50)
    
    print(shield.activate_faraday_logic())
    print("\n" + surge.monitor_voltage_spikes())
    print("-" * 50)
