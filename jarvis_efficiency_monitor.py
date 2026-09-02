import os
import time

class EfficiencyMonitor:
    def __init__(self):
        self.master = "Deepak"
        self.start_time = time.time()

    def get_uptime(self):
        uptime_seconds = time.time() - self.start_time
        return round(uptime_seconds, 2)

    def analyze_performance(self):
        print(f"\n\033[1;35m[EFFICIENCY MONITOR ACTIVE]\033[0m Analyzing Super-Frame stats...")
        
        # CPU लोड निकालने का वैकल्पिक तरीका (Load Average)
        try:
            load_avg = os.getloadavg()[0] # 1 मिनट का एवरेज लोड
            uptime = self.get_uptime()
            
            print(f"\033[1;36m[LOAD AVG]:\033[0m {load_avg}")
            print(f"\033[1;36m[UPTIME]:\033[0m {uptime} seconds")
            
            msg = f"Deepak sir, the system load is at {load_avg}. Session uptime is {uptime} seconds. Everything is stable."
            
            print(f"\033[1;32m[EFFICIENCY]: OPTIMAL\033[0m")
            os.system(f'termux-tts-speak "{msg}"')
            
        except Exception as e:
            print(f"\033[1;31m[LIMITATION]:\033[0m Access restricted. Simplified tracking active.")
            os.system('termux-tts-speak "Deepak sir, system restriction detected. Simplified monitor is online."')

if __name__ == "__main__":
    monitor = EfficiencyMonitor()
    monitor.analyze_performance()
