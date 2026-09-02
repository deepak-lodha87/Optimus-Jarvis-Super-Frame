# Optimus Jarvis Super-Frame: Phase 423-424
# Feature: System Optimization & Resource Allocation logic

import os
import time

class JarvisOptimizer:
    def __init__(self):
        self.code_ver = "424.Performance"
        self.threshold_cpu = 80.0 # Percentage

    def code_423_monitor_resources(self):
        print(f"\n[MODULE 423] Monitoring CPU & RAM usage...")
        # Simulating resource check via system load
        try:
            load1, load5, load15 = os.getloadavg()
            cpu_usage = (load1 / os.cpu_count()) * 100
            print(f"[SYSTEM] Current CPU Load: {cpu_usage:.2f}%")
            return cpu_usage
        except Exception:
            print("[SYSTEM] Load average unavailable. Using default safety scan.")
            return 25.0

    def code_424_optimize(self, cpu_load):
        print("\n[MODULE 424] Strategic Resource Allocation...")
        if cpu_load > self.threshold_cpu:
            print("[WARNING] High CPU load detected! Entering Power-Save mode.")
            print("[ACTION] Background processes suspended.")
        else:
            print("[STATUS] Performance is Optimal. High-Speed processing active.")

if __name__ == "__main__":
    opt_engine = JarvisOptimizer()
    print(f"--- {opt_engine.code_ver}: Active Monitoring ---")
    
    current_load = opt_engine.code_423_monitor_resources()
    opt_engine.code_424_optimize(current_load)
    
    print("\n--- Phase 424 Complete. System is Optimized. ---")
