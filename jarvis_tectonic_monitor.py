import time
import random

class TectonicOracle:
    def __init__(self):
        self.richter_scale = 0.0
        self.magma_pressure = 450 # psi

    def monitor_plates(self):
        print(f"\033[1;36m[GEOLOGY]\033[0m Scanning Tectonic Plate boundaries...")
        time.sleep(2)
        
        # Simulating seismic activity
        self.richter_scale = random.uniform(1.2, 4.5)
        self.magma_pressure += random.randint(10, 100)
        
        print(f" \033[1;32m[SEISMIC]\033[0m Activity Level: {self.richter_scale:.1f} Magnitude")
        print(f" \033[1;33m[MAGMA]\033[0m Sub-surface Pressure: {self.magma_pressure} PSI")
        
        if self.richter_scale > 4.0:
            print("\033[1;31m[ALERT]\033[0m Significant Tectonic Shift Detected. Monitoring for aftershocks.")
        else:
            print("\033[1;34m[STATUS]\033[0m Geological stability within safe parameters.")
            
        print(f"\n\033[1;35m[VOICE] Deepak sir, I can feel the heartbeat of the \nEarth itself. From the shifting plates to the \nrising magma, nothing moves beneath your \nfeet without my knowledge.\033[0m")

if __name__ == "__main__":
    oracle = TectonicOracle()
    oracle.monitor_plates()
