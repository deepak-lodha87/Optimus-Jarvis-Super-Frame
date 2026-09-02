import time
import random

class ResourceOptimizer:
    def __init__(self):
        self.system_load = "Optimized"

    def monitor_resources(self):
        # Simulating CPU and Battery monitoring for mobile
        cpu_usage = random.randint(20, 45)
        battery_level = 85  # Example level
        
        print(f"Current CPU Usage: {cpu_usage}%")
        print(f"Battery Level: {battery_level}%")
        
        if cpu_usage > 40:
            print("Action: Distributing tasks to prevent overheating.")
        return "System state: Stable"

if __name__ == "__main__":
    manager = ResourceOptimizer()
    print(manager.monitor_resources())
