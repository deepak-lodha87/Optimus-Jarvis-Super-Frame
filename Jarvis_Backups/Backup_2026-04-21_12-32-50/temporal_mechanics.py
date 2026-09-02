import time
import math

class TemporalCore:
    def __init__(self):
        self.c = 299792458 # Speed of light in m/s
        self.earth_time_seconds = 3600 # 1 Hour on Earth

    def phase_2649(self):
        print("\033[1;35m>> INITIATING: [SYSTEM_ROOT_2649] - Time-Dilation Calculation\033[0m")
        print("[LOG] Syncing atomic clocks with Earth's primary node...")
        time.sleep(1.2)
        
        # Unique Logic: Lorentz Factor Calculation
        velocity = 0.95 * self.c # 95% speed of light
        lorentz_factor = 1 / math.sqrt(1 - (velocity**2 / self.c**2))
        
        dilated_time = self.earth_time_seconds / lorentz_factor
        print(f"[ACT] Velocity: 95% of 'c' | Lorentz Factor: {lorentz_factor:.2f}")
        time.sleep(1.5)
        print(f"[RES] While 60 mins pass on Earth, only {dilated_time/60:.2f} mins pass for Jarvis.")

    def phase_2650(self):
        print("\n\033[1;34m>> INITIATING: [SYSTEM_ROOT_2650] - Temporal Synchronization\033[0m")
        print("[LOG] Adjusting system logs to compensate for relativistic drift...")
        time.sleep(1)
        
        print("[ACT] Stabilizing chronometric pulses...")
        time.sleep(1.2)
        print("[RES] Synchronization Complete. System time is now relative to the current vector.")
        print("\033[1;32m>> STATUS: TEMPORAL MECHANICS ACTIVE\033[0m")

if __name__ == "__main__":
    temporal = TemporalCore()
    temporal.phase_2649()
    temporal.phase_2650()
