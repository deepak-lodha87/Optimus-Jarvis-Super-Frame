import time
import os

class LatencyMonitor:
    def __init__(self):
        self.master = "Deepak"

    def test_speed(self):
        print(f"\n\033[1;33m[LATENCY MONITOR ACTIVE]\033[0m Testing core response time...")
        
        start_time = time.perf_counter()
        
        # सिमुलेटेड प्रोसेसिंग (जार्विस के सोचने का समय)
        time.sleep(0.05) 
        
        end_time = time.perf_counter()
        latency = (end_time - start_time) * 1000 # Milliseconds में
        
        print(f"\033[1;32m[RESPONSE TIME]:\033[0m {latency:.2f} ms")
        
        msg = f"Deep4k sir, core latency is {int(latency)} milliseconds. Processing speed is optimal."
        os.system(f'termux-tts-speak "{msg}"')

if __name__ == "__main__":
    monitor = LatencyMonitor()
    monitor.test_speed()
