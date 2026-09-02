import time

class OptimusDiagnostics:
    def __init__(self):
        # Blueprint specs for comparison
        self.blueprint_limits = {"temp": 105, "rpm_idle": 1000}

    def monitor_live_feed(self, current_temp, current_rpm):
        print("\033[1;36m>> OPTIMUS JARVIS: MONITORING ENGINE VITALS <<\033[0m")
        time.sleep(1)
        
        print(f"[DATA] Temp: {current_temp}°C | RPM: {current_rpm}")
        
        # Strategic Analysis Logic
        if current_temp > self.blueprint_limits["temp"]:
            print("\033[1;31m[CRITICAL] OVERHEATING DETECTED! Check cooling system.\033[0m")
        elif current_rpm > self.blueprint_limits["rpm_idle"]:
            print("\033[1;33m[ADVISORY] High Idle RPM. Possible throttle sensor defect.\033[0m")
        else:
            print("\033[1;32m[NORMAL] System operating within blueprint parameters.\033[0m")

if __name__ == "__main__":
    diag = OptimusDiagnostics()
    # Simulating live data from Phase 3002
    diag.monitor_live_feed(92, 850) 
